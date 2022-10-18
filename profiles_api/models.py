from operator import truediv
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


# Create your models here.

class UserProfileManager(BaseUserManager):
    """manager for user model profiles"""

    def create_user(self, email, name, password=None):
        """for creating user"""
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create superuser for model with given information"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Model for managing users in database"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_actice = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_first_name(self):
        """getting the first name of the user"""
        return self.name

    def __str__(self):
        """string representaion of the model"""
        return self.email


class ProfileFeeditem(models.Model):
    """storing user profile status"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """string represention for feed item of the user asociated with"""
        self.status_text

