from django.db import models
from datetime import datetime

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Users(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.username

class ModelsList(models.Model):
    user= models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=100,blank=True)
    description=models.TextField(blank=True)
    data=models.DateTimeField(default=datetime.now,blank=True)
    code=models.BooleanField(default=False) 
    snippet=models.TextField(blank=True)
    def __str__(self):
        return self.title

@receiver(post_save, sender=Users)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)