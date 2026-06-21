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

def task_list(req):
    task_data = TaskModel.objects.filter(created_by = req.user)
    
    context = {
        'task_data' : task_data
    }
    return render(req,'task_list.html',context)

def task_add(req):
    cur_user = req.user
    if req.method == 'POST':
        title = req.POST.get('title')
        description = req.POST.get('description')
        status = req.POST.get('status')
        deadline = req.POST.get('deadline')
        
        TaskModel.objects.create(
            title = title,
            description = description,
            status = status,
            deadline = deadline,
            created_by = cur_user
        )
        return redirect('task_list')
            
    return render(req,'task_add.html')

def task_update(req,id):
    cur_user = req.user
    task_up = TaskModel.objects.get(id = id)
    if req.method == 'POST':
        title = req.POST.get('title')
        description = req.POST.get('description')
        status = req.POST.get('status')
        deadline = req.POST.get('deadline')
        
        task_up.title = title
        task_up.description = description
        task_up.status = status
        task_up.deadline = deadline
        task_up.created_by = cur_user
        task_up.save()
        return redirect('task_list')
    
    context = {
        'task_up' : task_up
    }
    
    return render(req,'task_update.html',context)
        
        
        
    