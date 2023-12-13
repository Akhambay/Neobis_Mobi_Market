from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    DOB = models.DateField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, unique=True,
                                    help_text='Contact phone number', max_length=20)
