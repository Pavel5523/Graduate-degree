from django.forms import ModelForm
from .models import Flashcards


class FlashcardForm(ModelForm):
    class Meta:
       model = Flashcards
       fields = ['subject', 'term' , 'meaning']