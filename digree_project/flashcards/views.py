from django.shortcuts import render

def signupuser(request):
    return render(request, 'flashcards/signupuser.html')

def home(request):
    return render(request, 'flashcards/home.html')
