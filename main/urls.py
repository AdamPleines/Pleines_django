from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.index, name="index"),
    path("<int:id>", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("about", views.about, name="about"),
    path("product/", views.product_detail, name="product"),
    path("product", views.product_detail, name="product"),
    path("new/", views.product_new, name="new_product"),
    path("new", views.product_new, name="new_product"),
    path("v1/", views.v1, name="view 1"),
    path("v1", views.v1, name="view 1"),
]