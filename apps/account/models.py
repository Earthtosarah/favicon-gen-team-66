from ast import BinOp
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, editable=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __s
    tr__ (self) -> any:
        return self.name
