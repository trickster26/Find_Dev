from email.policy import default
from hashlib import blake2b
import profile
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profiless(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro_indus = models.CharField(max_length=200,blank=True,null=True)
    detail_dis = models.TextField(blank=True,null=True)
    indus_image = models.ImageField(null = True, blank=True,upload_to = 'indus/',default="profiles/user-default.png")
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_Website = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                          primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.user.username)
    
class ReqSkill(models.Model):
    owner = models.ForeignKey(Profiless,on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                          primary_key=True,editable=False)
    def __str__(self):
        return str(self.name)