from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username=models.CharField(max_length=250, unique=True)
    email=models.EmailField(max_length=50)
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('author', 'Author'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    avatar=models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"{self.username}"
