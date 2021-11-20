from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *

# Create your views here.

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")
def logout(request):
    return render(request,"logout.html")
# def updateprofile(request):
#     return render(request,"updateprofile.html")
# def cdclogin(request):
#     return render(request,"cdclogin.html")
    
    # if request.method== "POST":
    #      dept= request.POST['dept']
    #      email= request.POST['email']
    #      address= request.POST['address']
    #      username= request.POST['username']
    #      password1= request.POST['password1']
    #      password2= request.POST['password2']





# def testlogin(request):
#     return render(request,"testlogin.html")


def login(request):
    if request.method== "POST":
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect("updateprofile")

        else:
            messages.info(request,'INVALID')
            return redirect('login.html')
            
    else:
      return render(request,"login.html")


def signup(request):
     if request.method== "POST":
         first_name= request.POST['first_name']
         last_name= request.POST['last_name']
         email= request.POST['email']
         address= request.POST['address']
         username= request.POST['username']
         password1= request.POST['password1']
         password2= request.POST['password2']

         if password1==password2:
             if User.objects.filter(username=username).exists():
                 print('Username Taken')
             elif User.objects.filter(email=email).exists():
                print('email taken')
             else:
                 hr_signup( first_name= first_name, last_name= last_name, email=email, address=address, username=username, password=password1)
                 user=User.objects.create_user( email=email, username=username, password=password1)
                 user.save()
                 print('user created')
                 return redirect('/login')

         
         else: 
             print('Password is not matching..')   
             return redirect('/')


     else:
         return render(request,"signup.html")

#This is for update profile

def updateprofile(request):
    if request.method== "POST":
        dept=request.POST['dept']
        year=request.POST['year']
        rollno=request.POST['rollno']
        skills=request.POST['skills']

        hr_models(dept=dept,year=year,rollno=rollno,skills=skills)

    else:
        return render (request,'updateprofile.html')

   
    
