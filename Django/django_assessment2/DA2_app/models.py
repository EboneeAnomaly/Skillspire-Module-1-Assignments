from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField()
    description = models.TextField()

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, default='')  

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

