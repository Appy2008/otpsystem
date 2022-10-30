from email.policy import default
from ftplib import MAXLINE
from pyexpat import model
from  django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name= 'profile')
    email = models.EmailField(max_length = 254)
    otp = models.CharField(max_length=100,null= True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4)