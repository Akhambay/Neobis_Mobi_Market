from django.urls import path
from .views import ProductList, ProductDetail
from rest_framework.routers import DefaultRouter

users_router = DefaultRouter()

urlpatterns = [
    path("<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("", ProductList.as_view(), name="product_list"),
]
