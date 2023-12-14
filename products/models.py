from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    product_image = models.ImageField(
        null=True, blank=True, default='default_pic.jpg', upload_to='product_pics')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
