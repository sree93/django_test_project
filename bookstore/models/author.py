from django.db import models


class Author(models.Model):

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    CHOICES_GENDER = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    )

    name = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.CharField(max_length=8, choices=CHOICES_GENDER)
