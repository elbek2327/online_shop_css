from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products-of-category/<int:category_id>/', views.index, name='products_of_category'),
    path('popular/', views.popular_products, name="popular_products"),
    path('new_arrivals/', views.new_arrivals, name="new_arrivals"),
    path('product/<int:product_id>/', views.product_detail, name='products_of_category')
]
