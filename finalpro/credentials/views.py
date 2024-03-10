from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == 'POST':
        userName=request.POST['username']
        passWord=request.POST['password']
        user=auth.authenticate(username=userName,password=passWord)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('credentialsapp:login')

    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['Email']
        password=request.POST['Password']
        cpassword=request.POST['password']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect('credentialsapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('credentialsapp:register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,password=password,
                                              last_name=last_name,email=email)
                user.save()
                return redirect('credentialsapp:login')
        else:
            messages.info(request,"password not matching")
            return redirect('credentialsapp:register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')