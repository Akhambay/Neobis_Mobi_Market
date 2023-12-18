# Generated by Django 4.1 on 2023-12-18 18:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
