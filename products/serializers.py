from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'short_description',
                  'description', 'price', 'product_image', 'likes']
        read_only_fields = ['author', 'likes']
        model = Product
