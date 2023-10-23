from django.db import models
from django.contrib.auth.models import User

class Flashcards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True, verbose_name='Категория')
    term = models.CharField(max_length=100, verbose_name='Термин')
    meaning = models.CharField(max_length=250, verbose_name='Значение')
    term_photo = models.ImageField(upload_to='photos', blank=True, null=True)
    meaning_photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return f'{self.subject} {self.term} {self.meaning}'

# Create your models here.
