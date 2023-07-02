from django.shortcuts import render, redirect
from .models import City
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def index(request):
    projects = City.objects.all()
    return render(request, 'info/index.html', {'projects': projects})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'info/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'info/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя уже существует'})
        else:
            return render(request, 'info/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logoutuser(request):
    logout(request)
    return redirect('signupuser')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'info/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'info/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Такого пользователя не существует'})
        else:
            login(request, user)
            return redirect('index')

# Create your views here.
