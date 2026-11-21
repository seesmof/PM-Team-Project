from django.urls import path

from clicks import views

urlpatterns = [
    path("/status", views.status, name="status"),
]
