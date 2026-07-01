"""Config-driven, region-scoped admin panels.

For every region in ``settings.REGIONS`` a separate admin site is generated at
``/admin/<code>/`` (e.g. ``/admin/uae/``, ``/admin/us/``). Each one:

* shows ONLY that region's rows (querysets filtered by region),
* auto-stamps the region on everything you create there (region field hidden),
* filters foreign-key dropdowns (e.g. Category) to the same region,
* is branded so you always know which region you're editing.

Adding a new country later = add one entry to ``settings.REGIONS``; its admin
panel, filtering and branding all appear automatically — no extra code.

The default ``/admin/`` stays as a master site (superusers see every region).
"""

from django.conf import settings
from django.contrib import admin


class RegionAdminSite(admin.AdminSite):
    """An admin site locked to a single region."""

    def __init__(self, name, region):
        super().__init__(name=name)
        self.region_code = region["code"]
        self.site_header = f"Brockwell {region['short']} — Administration"
        self.site_title = f"Brockwell {region['short']} Admin"
        self.index_title = f"Manage the {region['name']} website"


class RegionScopedAdminMixin:
    """Mixes into any ModelAdmin to scope it to ``self.admin_site.region_code``.

    ``region_lookup`` is the ORM path used to filter the queryset; ``region_field``
    is the direct field to auto-set on save (None when the region is inferred
    through a relation, e.g. an event registration).
    """

    region_lookup = "region"
    region_field = "region"

    def _region(self):
        return getattr(self.admin_site, "region_code", None)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        code = self._region()
        if code and self.region_lookup:
            qs = qs.filter(**{self.region_lookup: code})
        return qs

    def get_fieldsets(self, request, obj=None):
        """Hide the region field — it is set automatically for this panel."""
        fieldsets = super().get_fieldsets(request, obj)
        code = self._region()
        if not code or not self.region_field:
            return fieldsets
        cleaned = []
        for name, opts in fieldsets:
            opts = dict(opts)
            if "fields" in opts:
                opts["fields"] = tuple(
                    f for f in opts["fields"] if f != self.region_field
                )
            cleaned.append((name, opts))
        return cleaned

    def save_model(self, request, obj, form, change):
        code = self._region()
        if code and self.region_field and hasattr(obj, self.region_field):
            setattr(obj, self.region_field, code)
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        """Stamp the region onto inline rows (e.g. sub-services) too."""
        code = self._region()
        instances = formset.save(commit=False)
        for instance in instances:
            if code and hasattr(instance, "region"):
                instance.region = code
            instance.save()
        formset.save_m2m()
        for obj in formset.deleted_objects:
            obj.delete()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        code = self._region()
        rel = db_field.related_model
        if code and rel is not None and _model_field_names(rel).__contains__("region"):
            kwargs["queryset"] = rel._default_manager.filter(region=code)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


def _model_field_names(model):
    return {getattr(f, "name", None) for f in model._meta.get_fields()}


def _region_scope_for(model):
    """Return (region_lookup, region_field) for a model, or (None, None) if the
    model has no region concept (those stay off the region panels)."""
    names = _model_field_names(model)
    if "region" in names:
        return "region", "region"
    if "event" in names:  # e.g. EventRegistration -> event.region
        return "event__region", None
    return None, None


def build_region_admin_sites():
    """Create one RegionAdminSite per configured region and register every
    region-aware model on it (reusing each model's existing ModelAdmin config)."""
    sites = {}
    for region in settings.REGIONS.values():
        site = RegionAdminSite(f"{region['code']}_admin", region)
        for model, model_admin in admin.site._registry.items():
            lookup, field = _region_scope_for(model)
            if lookup is None:
                continue  # not a region model (e.g. auth User/Group) — master only
            scoped = type(
                f"Regional{model_admin.__class__.__name__}",
                (RegionScopedAdminMixin, model_admin.__class__),
                {"region_lookup": lookup, "region_field": field},
            )
            site.register(model, scoped)
        sites[region["code"]] = site
    return sites
