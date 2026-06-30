from django.conf import settings
from django.shortcuts import get_object_or_404, render

from core import seo
from core.regions import region_path

from .models import Doctor


def team_list(request):
    region = request.region
    doctors = Doctor.objects.filter(region=region["code"], is_published=True)

    meta = seo.build_meta(
        request,
        title=f"Our Team in {region['name']}",
        description=(
            f"Meet the experienced clinicians and specialists at {settings.BRAND_NAME} "
            f"in {region['name']} — dedicated to your regenerative health and longevity."
        ),
        path="/team/",
    )
    jsonld = [
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Our Team", meta["canonical"]),
            ]
        )
    ]
    jsonld += [seo.doctor_schema(d, region) for d in doctors]

    return render(
        request,
        "team/list.html",
        {"meta": meta, "jsonld": jsonld, "doctors": doctors},
    )


def doctor_detail(request, slug):
    region = request.region
    doctor = get_object_or_404(Doctor, region=region["code"], slug=slug, is_published=True)
    others = Doctor.objects.filter(region=region["code"], is_published=True).exclude(pk=doctor.pk)[:3]

    title = doctor.seo_title or f"{doctor.name} — {doctor.title}"
    description = doctor.seo_description or doctor.short_bio
    meta = seo.build_meta(
        request, title=title, description=description, path=f"/team/{doctor.slug}/", og_type="profile"
    )
    jsonld = [
        seo.doctor_schema(doctor, region),
        seo.breadcrumb_schema(
            [
                ("Home", seo.absolute(region_path(region["code"], "core:home"))),
                ("Our Team", seo.absolute(region_path(region["code"], "team:list"))),
                (doctor.name, meta["canonical"]),
            ]
        ),
    ]
    return render(
        request,
        "team/detail.html",
        {"meta": meta, "jsonld": jsonld, "doctor": doctor, "others": others},
    )
