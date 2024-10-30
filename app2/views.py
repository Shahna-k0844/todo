from django.contrib import messages

from email import message
from venv import create
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from.models import *
from django.contrib.auth import authenticate,login,logout


from .models import *
# Create your views here.
def homefunction(request):

    if request.method =='POST':
        title=request.POST.get('title')
        details=request.POST['details']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        final=Todo.objects.create(title=title,details=details,startdate=startdate,enddate=enddate)
        final.save()
        return redirect('show')
        # finalcall=Todo.objects.all()
        # print(title)
    # finalcall.delete()
    # if not finalcall:
        
    return render(request,'home.html')
def showfunction(request):
    finalcall=Todo.objects.all()

    return render(request,'show.html',{'final':finalcall})
def removefunction(request,id):

    remove=Todo.objects.get(id=id)
    remove.delete()
    return redirect('show')
def editfunction(request,id):
    edit=Todo.objects.get(id=id)
    if request.method =='POST':
        title=request.POST.get('title')
        details=request.POST['details']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        # final=Todo.objects.create(title=title,details=details,startdate=startdate,enddate=enddate)
        # edit.save()
            
        if edit:
            edit.title=title
            edit.details=details
            edit.startdate=startdate
            edit.enddate=enddate
            edit.save()
        return redirect('show')
    return render(request,'edit.html',{'edit':edit})
def signfunction(request):
    if request.method=='POST':
        username=request.POST['username']   
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username,email,password)
        user.save()
    return render(request,'sign.html')    
def loginfunction(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'try again')
            return redirect('sign') 
    return render(request,'login.html')