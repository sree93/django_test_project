from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.ForeignKey('bookstore.Author', on_delete=models.CASCADE)


