from django.db import models
from django.contrib.auth.models import User

class Flashcards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True)
    term = models.CharField(max_length=100)
    meaning = models.CharField(max_length=250)
    term_photo = models.ImageField(upload_to='photos', blank=True, null=True)
    meaning_photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return f'{self.term} {self.subject}'

# Create your models here.
