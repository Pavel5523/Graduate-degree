from django.forms import ModelForm
from .models import Flashcards
# from django .contrib.auth.forms import UserCreationForm

# class RegisterUserForm(UserCreationForm):



class FlashcardForm(ModelForm):
    class Meta:
       model = Flashcards
       fields = ['subject', 'term' , 'meaning']