from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth


# Create your views here.


def home(request):
    return render(request, 'account/home.html')


def signupuser(request):
    # localhost:8000/SignUp/
    if request.method == 'GET':
        return render(request, 'account/signup.html', {'form': CreateUserForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                messages.success(request, 'Your Account is been created ')
                login(request, user)
                return redirect('loginuser')
            except IntegrityError:
                return render(request, 'account/signup.html', {'form': CreateUserForm(), 'error': 'That username has already been taken. Please choose a new username'})

        else:
            return render(request, 'account/signup.html', {'form': CreateUserForm(), 'error': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'account/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Invalid login credentials')
            return render(request, 'account/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('index')


@login_required
def logoutuser(request):
    auth.logout(request)
    messages.success(request, 'You are logged out! Wanna LogIn Again')
    return redirect('loginuser')
