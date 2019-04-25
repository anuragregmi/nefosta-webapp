from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    introduction = models.CharField(max_length=250)
    phone_number = models.CharField(
        max_length=15, unique=True,
        null=True, blank=True
    )
    profile_picture = models.ImageField(
        upload_to="profile-pics/",
        null=True,
        blank=True
    )
