from email import message
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profiles
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.utils.html import strip_tags

    
def createProfile(sender , instance ,created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(
            user =user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = "Welcome to Find.Dev"
        # message = ["Hi User,"
        #            "Welcome to Find.Dev – we’re excited to have you on board and we’d love to say thank you on behalf of our whole Team for chosing us."
        #            "We believe our site will help you in connecting with Developer."
        #            "Have any questions , need more information or Want to give any feedback? Just shoot us an email! We’re always here to help."
        #            "Take care,"
        #            "Find.Dev Team"]
        # message = "we are glade you are here!"

        html_message = render_to_string('mail.html', {'name': user.first_name })
        message = strip_tags(html_message)

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently = False,
            html_message=html_message, 
        )

def updateUser(sender , instance, created,  **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

       
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
        

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender= Profiles)
post_delete.connect(deleteUser, sender= Profiles)