from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description', 'price', 'product_image']
        read_only_fields = ['author']
        model = Product
