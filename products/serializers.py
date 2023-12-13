from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "title",
            "description",
            "price",
            "product_image",
            "author",
        )
        model = Product
