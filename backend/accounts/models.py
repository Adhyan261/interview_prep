from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(unique=True,max_length=20)
    email = models.EmailField(unique=True)
    about = models.TextField(blank= True)
    # Add custom fields here, if needed

    def __str__(self):
        return self.username