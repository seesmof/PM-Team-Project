from django.urls import path

from clicks import views

urlpatterns = [
    path("", views.index, name="index"),
]
