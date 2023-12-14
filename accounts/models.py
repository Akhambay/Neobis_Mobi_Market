from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    DOB = models.DateField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, unique=True,
                                    help_text='Contact phone number', max_length=20)
    profile_image = models.ImageField(
        null=True, blank=True, default='default.jpg', upload_to='profile_pics')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}'
