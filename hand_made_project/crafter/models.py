from django.contrib.auth.models import User
from django.db import models


class CrafterPerson(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    category = models.ForeignKey(to='CategoryCrafter', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoryCrafter(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title
