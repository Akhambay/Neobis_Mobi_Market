from django.urls import path, include
from .views import ProductList, ProductDetail, UserProductListView, ProductCreateView, LikedProductListView, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path("products/all", ProductList.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path('products/my-list/', UserProductListView.as_view(), name='my-list'),
    path('products/add/', ProductCreateView.as_view(), name='create-product'),
    path('api/products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/liked/', LikedProductListView.as_view(), name="products_liked"),
]
