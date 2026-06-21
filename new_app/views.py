from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from new_app.models import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'User login successfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Invalid credentials.')
            return redirect('login_view')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')
        
        user_exist = UserModel.objects.filter(username = username).exists()
        if user_exist:
            messages.warning(request, 'User already exists.')
            return redirect('register_view')
        
        if password == conf_password:
            UserModel.objects.create_user(
                username=username,
                full_name = full_name,
                email = email,
                password= password,
            )
            messages.success(request, 'User created successfully')
            return redirect('login_view')
        else:
            messages.warning(request, 'Password doesnot match.')
            return redirect('register_view')

    return render(request, 'register.html')

@login_required
def dashboard(request):


    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('login_view')