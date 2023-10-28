from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FlashcardForm
from .models import *
from random import randint
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signupuser(request):  # Функция создания пользователя
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


@login_required
def home(request):  # Функция домашней страницы
    if request.method == 'POST':
        logout(request)
        return redirect('come')
    else:
        return render(request, 'flashcards/home.html')


def start(request):  # Функция стартовой страницы
    return render(request, 'flashcards/start.html')


def come(request):  # Функция страницы авторизации
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


@login_required
def logoutuser(request):  # Функция разлогинивания
    if request.method == 'POST':
        logout(request)
        return redirect('start')


@login_required
def create_flashcard(request):  # Функция создания карточек
    if request.method == 'GET':
        return render(request, 'flashcards/create_flashcard.html', {'form': FlashcardForm()})
    else:
        try:
            form = FlashcardForm(request.POST)
            new_flashcard = form.save(commit=False)
            new_flashcard.user = request.user
            new_flashcard.save()
            messages.success(request, 'Карточка созданна успешно')
            return redirect('create_flashcard')
        except ValueError:
            return render(request, 'flashcards/create_flashcard.html',
                          {'form': FlashcardForm(),
                           'error': 'Заполненны неверные данные попробуйте еще раз'})


@login_required
def flashcard(request):  # Функция просмотра существующих карточек
    flashcards = Flashcards.objects.filter(user=request.user)
    return render(request, 'flashcards/flashcard.html', {'flashcards': flashcards})


@login_required
def delete_flashcard(request, flashcard_pk):  # Функция удаленя карточек
    flashcard = get_object_or_404(Flashcards, pk=flashcard_pk, user=request.user)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('flashcard')


@login_required
def back_home(request):  # Функция возврата на домашнюю страницу
    return redirect(request, 'flashcard')


@login_required
def education(request):  # Функция обучения с помощью карточек
    flashcard = Flashcards.objects.filter(user=request.user)
    random_card = flashcard[randint(0, len(flashcard) - 1)]
    return render(request, 'flashcards/education.html', {'flashcard': random_card})
