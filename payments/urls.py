from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path("success/", views.checkout_success, name="success"),
    path("cancel/", views.checkout_cancel, name="cancel"),
]
