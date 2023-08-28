from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FlashcardForm


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
    logout(request)
    return render(request, 'flashcards/home.html')


def start(request):
    return render(request, 'flashcards/start.html')


def come(request):
    if request.method == 'GET':
        return render(request, 'flashcards/come.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'flashcards/come.html',
                          {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})

        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('start')


def flashcard(request):
    if request.method == 'GET':
        return render(request, 'flashcards/flashcard.html')


def create_flashcard(request):
    if request.method == 'GET':
        return render(request, 'flashcards/create_flashcard.html', {'form': FlashcardForm()})
    else:
        try:
            form = FlashcardForm(request.POST)
            new_flashcard = form.save(commit=False)
            new_flashcard.user = request.user
            new_flashcard.save()
            return redirect('create_flashcard.html', {'error': 'Карточка созданна успешно'})
        except ValueError:
            return render(request, 'flashcards/create_flashcard.html',
                          {'form': FlashcardForm(),
                        'error': 'Заполненны неверные данные попробуйте еще раз'})

# Create your views here.
