from django.db import models
from django.contrib.auth.models import User 


class Book(models.Model):
    name = models.CharField(max_length=50)
    book_description = models.CharField(max_length=500)
    image = models.ImageField()


    def __str__(self):
        return f"Name: {self.name} //// book_description: {self.book_description} //// image: {self.image}"