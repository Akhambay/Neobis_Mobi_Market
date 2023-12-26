from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.PositiveIntegerField()
    product_image = models.ImageField(
        null=True, blank=True, default='/product_pics/default.jpg', upload_to='product_pics')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='liked_products', blank=True)

    def total_likes(self):
        return self.likes.count()

    def user_like(self, user):
        return self.likes.filter(pk=user.pk).exists()

    def __str__(self):
        return self.title
