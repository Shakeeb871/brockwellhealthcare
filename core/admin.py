from django.contrib import admin

from .models import ContactLead, FAQ


@admin.register(ContactLead)
class ContactLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "region", "handled", "created_at")
    list_filter = ("region", "handled", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_editable = ("handled",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "region", "order", "is_published")
    list_filter = ("region", "is_published")
    search_fields = ("question", "answer")
    list_editable = ("order", "is_published")


admin.site.site_header = "Stem Cell — Site Administration"
admin.site.site_title = "Site Admin"
admin.site.index_title = "Manage your website content"
