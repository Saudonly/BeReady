from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import HumanResourceProfile 

# Create your views here.

def register_user(request : HttpRequest):
    ''' This function will create a new user'''

    if request.method == "POST":

        new_user = User.objects.create_user(first_name=request.POST["first_name"],last_name=request.POST["last_name"],username=request.POST["username"], email= request.POST["email"], password=request.POST["password"])
        new_user.save()
        return redirect("BeReady:home")
        
    return render(request, "accounts/register.html")
    

def register_human_resource(request : HttpRequest):
    ''' This function will create a human resource user'''

    if request.method == "POST":

        new_hr = User.objects.create_user(first_name=request.POST["first_name"],last_name=request.POST["last_name"],username=request.POST["username"], email= request.POST["email"], password=request.POST["password"])
        new_hr.save()

        hr_profile = HumanResourceProfile(user=new_hr, field=request.POST["field"], desceiption=request.POST["desceiption"],image=request.FILES["image"])
        hr_profile.save()
        return redirect("BeReady:home")
        
    return render(request, "accounts/hr_register.html")


def login_user(request : HttpRequest):
    ''' This function will login a user'''
    massage: str = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        
        if user:
            login(request, user)
            return redirect("BeReady:base.html")
        else:
            massage = "User Not Found, Check Your Credentials"

    return render(request, "accounts/login.html", {"msg" : massage})


def logout_user(request: HttpRequest):
    ''' This function will logout a new user'''
    logout(request)

    return redirect("BeReady:base.html")

    