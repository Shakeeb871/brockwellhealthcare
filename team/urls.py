from django.urls import path

from . import views

app_name = "team"

urlpatterns = [
    path("", views.team_list, name="list"),
    path("<slug:slug>/", views.doctor_detail, name="detail"),
]
