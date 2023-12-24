# Generated by Django 4.2.8 on 2023-12-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_liked_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='liked_by',
            new_name='likes',
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]