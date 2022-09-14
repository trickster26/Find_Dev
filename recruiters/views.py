from multiprocessing import context
from django.shortcuts import render
from .models import Profiless
# Create your views here.

def profiless(request):
    profiles = Profiless.objects.all()
    context = {'profiles':profiles}
    return render(request, 'recruiters/profiless.html',context)

def userProfile(request,pk):
    profile = Profiless.objects.get(id=pk)
    context={'profile':profile}
    return render(request, 'recruiters/user-profile.html', context)