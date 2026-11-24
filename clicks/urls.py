from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("status/", views.status, name="status"),
    path("totals/", views.totals, name="totals"),
    path("delete/<int:id>", views.delete_client, name="delete"),
]
