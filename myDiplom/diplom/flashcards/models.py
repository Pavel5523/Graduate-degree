from django.db import models
from django.contrib.auth.models import User

class Flashcards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True)
    term = models.CharField(max_length=100)
    meaning = models.CharField(max_length=250)

    def __str__(self):
        return self.term

# Create your models here.
