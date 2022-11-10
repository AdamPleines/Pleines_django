from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.index, name="index"),
    path("<int:id>", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("about", views.about, name="about"),
    path("v1/", views.v1, name="view 1"),
    path("v1", views.v1, name="view 1"),
]