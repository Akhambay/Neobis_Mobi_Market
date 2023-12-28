from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        fields = ['id', 'title', 'short_description',
                  'description', 'price', 'product_image', 'likes', 'likes_count']
        read_only_fields = ['author', 'likes']
        model = Product

    def get_likes_count(self, obj):
        return obj.total_likes()
