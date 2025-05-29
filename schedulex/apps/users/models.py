from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def createUser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is a required field');
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.createUser(email, password, **extra_fields)
class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=200, unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
    
