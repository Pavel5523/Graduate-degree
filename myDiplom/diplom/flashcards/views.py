from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'flashcards/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'flashcards/signupuser.html',
                {'form': UserCreationForm(),
                'error': 'Такое имя пользователя уже существует. Выберите другое имя'})
        else:
            return render(request, 'flashcards/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})

def home(request):
    return render(request, 'flashcards/home.html')


def start(request):
    return render(request, 'flashcards/start.html')


def come(request):
    return render(request, 'flashcards/come.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('start')

# Create your views here.
