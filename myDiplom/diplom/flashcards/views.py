from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FlashcardForm
# from django.views.generic import ListView
from .models import *
from random import randint
from django.contrib import messages


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
    if request.method == 'POST':
        logout(request)
        return redirect('come')
    else:
        return render(request, 'flashcards/home.html')


def start(request):
    return render(request, 'flashcards/start.html')


def come(request):
    if request.method == 'GET':
        return render(request, 'flashcards/come.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
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


# def flashcard(request):
#     if request.method == 'GET':
#         return render(request, 'flashcards/flashcard.html')


def create_flashcard(request):
    if request.method == 'GET':
        return render(request, 'flashcards/create_flashcard.html', {'form': FlashcardForm()})
    else:
        try:
            form = FlashcardForm(request.POST)
            new_flashcard = form.save(commit=False)
            new_flashcard.user = request.user
            new_flashcard.save()
            messages.success(request, 'ooooooooo')
            # print(mess)
            return redirect('create_flashcard') #{'error': 'Карточка созданна успешно'})
        except ValueError:
            return render(request, 'flashcards/create_flashcard.html',
                          {'form': FlashcardForm(),
                           'error': 'Заполненны неверные данные попробуйте еще раз'})


def flashcard(request):
    flashcards = Flashcards.objects.filter(user=request.user)
    return render(request, 'flashcards/flashcard.html', {'flashcards': flashcards})


def delete_flashcard(request, flashcard_pk):
    flashcard = get_object_or_404(Flashcards, pk=flashcard_pk, user=request.user)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('flashcard')


def back_home(request):
    return redirect(request, 'flashcard')


def education(request):
    flashcard = Flashcards.objects.filter(user=request.user)
    # print(len(flashcard))
    # len_flashcard = len(flashcard)
    # for card in range(len_flashcard):
    #     len_flashcard -= 1
    #     print(len_flashcard)
    random_card = flashcard[randint(0, len(flashcard) - 1)]
    return render(request, 'flashcards/education.html', {'flashcard': random_card})


# def next(request):
#     return render(request, 'flashcards/education.html')

# Create your views here.
