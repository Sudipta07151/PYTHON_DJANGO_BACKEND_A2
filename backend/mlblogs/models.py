from django.db import models
from datetime import datetime
from django.utils import timezone


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.utils.translation import gettext_lazy as _


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager



class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    #password = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ModelsList(models.Model):
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True,max_length=1000)
    data = models.DateTimeField(default=datetime.now, blank=True)
    code = models.BooleanField(default=False)
    snippet = models.TextField(blank=True)

    def __str__(self):
        return self.title


# @receiver(post_save, sender=Users)
# def create_auth_token(sender, instance=Users, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
