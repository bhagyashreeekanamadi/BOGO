from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio=models.TextField(blank=True)
    image=models.URLField(blank=True)

