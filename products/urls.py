from django.urls import path
from .views import ProductList, ProductDetail, UserProductListView, ProductCreateView
from rest_framework.routers import DefaultRouter

users_router = DefaultRouter()

urlpatterns = [
    path("products/", ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path('products/my-list/', UserProductListView.as_view(), name='my-list'),
    path('products/add/', ProductCreateView.as_view(), name='create-product'),
]
