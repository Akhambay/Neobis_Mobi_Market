from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user

        if not user.user_verified:
            return Response({'detail': 'User is not verified. Please verify your account.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user)


class LikedProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author = self.request.user.id
        queryset = Product.objects.filter(likes__id=author)
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        product = self.get_object()
        user = request.user

        if user not in product.likes.all():
            product.likes.add(user)
            return Response({'status': 'Product liked'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'User already liked this product'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        product = self.get_object()
        user = request.user

        if user in product.likes.all():
            product.likes.remove(user)
            return Response({'status': 'Product unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'User did not like this product'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def likes_count(self, request, pk=None):
        product = self.get_object()
        count = product.total_likes()
        return Response({'likes_count': count}, status=status.HTTP_200_OK)
