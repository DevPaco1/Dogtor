from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import ModUserManager

class ModUser (AbstractBaseUser, PermissionsMixin):
    """Custom Moderator User"""

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    start_date =  models.DateTimeField(auto_now_add=True)
    about = models.TextField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = ModUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["user_name","first_name"]

    def __str__(self) -> str:
        return f"{self.user_name} {self.email}"