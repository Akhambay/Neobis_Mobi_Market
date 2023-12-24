from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        existing_product_image = serializer.instance.product_image
        serializer.save()

        if 'product_image' not in self.request.data or not self.request.data['product_image']:
            serializer.instance.product_image = existing_product_image
            serializer.instance.save()


class UserProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user)


class LikedProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        author = self.request.user.id
        queryset = Product.objects.filter(likes__id=author)
        return queryset
