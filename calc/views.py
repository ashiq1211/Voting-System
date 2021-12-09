from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

from calc.models import Destination
# Create your views here.
def home(request):
     return  render(request,'home.html')
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'Result':res})
def dest(request):
    dest=Destination.objects.all()
    return  render(request,'destination.html',{'dests':dest})
def register(request):
    if request.method=='POST':
        print("dshv jdhxbdfhjbdfjh")
        user_name=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
               user= User.objects.create_user(username=user_name,email=email,password=pass1)
               user.save()
               print("vhgvhvhvvhbjhjk")
               return redirect('/')
        else:
            messages.info(request,'Password didnt match')
            return redirect('register')
    else:

        return  render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:    
        return  render(request,'login.html')
def logout(request):
    auth.logout(request)
    return  redirect('/dest')
