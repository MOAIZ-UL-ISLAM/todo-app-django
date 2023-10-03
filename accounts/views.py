from django.shortcuts import render, redirect, HttpResponse
from django.http import request
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(f"username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful') 
            print("User authenticated successfully")
            return redirect('todos')
        else:
            messages.success(request, 'Login Error')
            print("User not authenticated")
            return render(request, 'accounts/login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html')



def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
    else:
        form =SignUpForm()
        return render(request, 'accounts/register.html',{'form':form})
    
    return render(request, 'accounts/register.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'accounts/home.html')
