from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .models import User


def create_manager():
    if not User.objects.filter(email='manager@gmail.com').first():
        user = User.objects.create_user(
            'manager@gmail.com', 'shop manager', 'manpass123'
        )
        user.is_manager = True
        user.save()


def manager_login(request):
    if request.method == 'POST':
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None and user.is_manager:
                login(request, user)
                return redirect('dashboard:products')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:manager_login')
        else:
            form = ManagerLoginForm()
        context = {'form': form}
        return render(request, 'manager_login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('1111111')
            user = User.objects.create_user(
                data['email'], data['full_name'], data['password']
            )
            print('222222')
            user.save()
            return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
    context = {'title': 'Signup', 'form': form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('shop:home_page')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger'
                )
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    context = {'title': 'Login', 'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')


def edit_profile(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your profile has been updated', 'success')
        return redirect('accounts:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'edit_profile.html', context)
