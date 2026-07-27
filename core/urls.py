from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    # Per-country LLM manifest (GEO), e.g. /uae/llms.txt. The root /llms.txt
    # for the default region is registered in config/urls.py.
    path("llms.txt", views.llms_txt, name="llms-region"),
    # Legal / content pages (editable in admin via the Page model).
    path("privacy-policy/", views.page, {"slug": "privacy-policy"}, name="privacy"),
    path("terms-conditions/", views.page, {"slug": "terms-conditions"}, name="terms"),
    path("cookies/", views.page, {"slug": "cookies"}, name="cookies"),
]
