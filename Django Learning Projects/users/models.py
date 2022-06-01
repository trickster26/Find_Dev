from cProfile import Profile
import email
import uuid
from pickle import TRUE
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE ,null= True , blank=True)
    name = models.CharField(max_length=200 , blank=True ,null=True)
    email = models.EmailField(max_length=500 ,blank=True, null=True)
    username = models.CharField(max_length=200 , blank=True ,null=True)
    location = models.CharField(max_length=200 , blank=True ,null=True)
    short_intro = models.CharField(max_length=200 , blank=True ,null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank =True ,upload_to ='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkdin = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        # -created islia takki new projects and new account front page pr ho we can change later
        # ordering = ['-created']
        #isko change krunga kuch random type dalunga
        ordering=['created']
    
    
    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url=""
            
        return url
    
class Skill(models.Model):
    owner = models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True,blank=True)
    name =  models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(null =True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.name)
    
    
class Message(models.Model):
    sender = models.ForeignKey(
        Profiles, on_delete=models.SET_NULL,null=True ,blank=True)
    # on_delete is for agar bnda apna account delete kr k bhi chla jjae tabhi reciever ko msg dikhega
    # null=True a person who does not have account can send message
    recipient = models.ForeignKey(
        Profiles, on_delete=models.SET_NULL,null=True ,blank=True,related_name="messages")
    name=models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.subject 
    class Meta:
        ordering=['is_read','-created']   
    