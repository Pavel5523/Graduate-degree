from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signupuser(request):
    return render(request, 'flashcards/signupuser.html', {'form': UserCreationForm})


def home(request):
    return render(request, 'flashcards/home.html')

# Create your views here.
