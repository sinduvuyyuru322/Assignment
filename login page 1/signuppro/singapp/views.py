from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def create(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['conform_password']

        if password != confirm_password:
            messages.error(request,"password does not match")
            return redirect("register")
        else:
            userdetails = User(username=username, email=email)
            userdetails.set_password(password)  # Hashes the password
            userdetails.save()
            return redirect('login/')
        
    return render(request,"signup.html")
def loginpage(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html")
def logoutpage(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")

        






