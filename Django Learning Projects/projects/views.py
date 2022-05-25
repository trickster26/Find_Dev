from multiprocessing import context
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator ,PageNotAnInteger , EmptyPage
from .models import Project, Tag
from .forms import ProjectForm
from django.db.models import Q
from .utils import searchProjects


def projects(request):
    
    projects ,search_query = searchProjects(request)
    
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects,results)
    
    try:
        projects =paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects = paginator.page(page)
    except EmptyPage:
        page  = paginator.num_pages
        projects=paginator.page(page)
      
    leftIndex = (int(page) - 4)
    
    
    if leftIndex <1:
        leftIndex=1
    
    rightIndex = (int(page) +5)
    
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    
    
    
    
      
      
    custom_range = range(leftIndex,rightIndex )
        
         
    context ={'projects':projects , 'search_query':search_query,'paginator':paginator,'custom_range':custom_range}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj,})


@login_required(login_url='login')
def createProject(request):
    profile= request.user.profiles
    form = ProjectForm()
    
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
            
    
    context ={'form': form}
    return render(request,"projects/project_form.html",context)



@login_required(login_url='login')
def updateProject(request,pk):
    profile =request.user.profiles
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
            
    
    context ={'form': form}
    return render(request,"projects/project_form.html",context)



@login_required(login_url='login')
def deleteProject(request,pk):
    profile =request.user.profiles
    project =profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context ={'object':project}
    return render (request,'delete_template.html',context)