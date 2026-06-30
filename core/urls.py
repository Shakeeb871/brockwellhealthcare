from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    # Legal / content pages (editable in admin via the Page model).
    path("privacy-policy/", views.page, {"slug": "privacy-policy"}, name="privacy"),
    path("terms-conditions/", views.page, {"slug": "terms-conditions"}, name="terms"),
    path("cookies/", views.page, {"slug": "cookies"}, name="cookies"),
]
