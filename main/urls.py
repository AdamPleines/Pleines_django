from django.urls import path

from . import views

# All the functional URLs I made need to be listed below for django to find them

urlpatterns = [
    path("", views.home, name="home"),
    path("product"+"<int:id>/", views.product_detail, name="product details"),
    path("product"+"<int:id>", views.product_detail, name="product details"),
    path("products/", views.product_index, name="product index"),
    path("products", views.product_index, name="product index"),
    path("<int:id>/", views.index, name="index"),
    path("<int:id>", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("about", views.about, name="about"),
    # path("product/", views.products, name="product"),
    # path("product", views.v1, name="product"),
    path("new/", views.product_new, name="product creation"),
    path("new", views.product_new, name="product creation"),
    path("v1/", views.v1, name="view 1"),
    path("v1", views.v1, name="view 1"),
]