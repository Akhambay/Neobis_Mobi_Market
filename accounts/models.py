from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    DOB = models.DateField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, unique=True,
                                    help_text='Contact phone number', max_length=20)
    profile_image = models.ImageField(
        null=True, blank=True, default='/profile_pics/default.png', upload_to='profile_pics')
    user_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'
