from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ADMIN = 'admin'
    ASSISTANT = 'assistant'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (ASSISTANT, 'Assistant'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ASSISTANT)
