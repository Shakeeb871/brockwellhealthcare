from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.service_overview, name="list"),
    path("<slug:category>/", views.category_detail, name="category"),
    path("<slug:category>/<slug:slug>/", views.service_detail, name="detail"),
    path(
        "<slug:category>/<slug:parent>/<slug:slug>/",
        views.service_detail,
        name="subdetail",
    ),
]
