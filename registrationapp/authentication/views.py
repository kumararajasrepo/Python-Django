from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from registrationapp import settings
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request,"authentication/index.html");

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        messages.success(request,"c")
        print("save 1")
        myuser.save()
        print("save 2")
        messages.success(request,"s")
        messages.success(request,"Account has been created successfully")   
        return redirect('signin') 
    else:
        messages.success(request,"b")
    return render(request,"authentication/signup.html")
    

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return render(request,"authentication/index.html")
        else:
            messages.error(request,'not authenticated')
            return redirect('home')
    
    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')
