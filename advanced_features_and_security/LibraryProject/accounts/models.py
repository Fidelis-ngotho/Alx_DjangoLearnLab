from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):      
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)



class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_accounts_set",  # Unique related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_accounts_permissions_set",  # Unique related_name
        blank=True,
    )

# Create your models here.
