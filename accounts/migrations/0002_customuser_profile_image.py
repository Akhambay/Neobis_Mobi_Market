# Generated by Django 4.0.10 on 2023-12-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]