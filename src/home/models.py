from django.db import models
from django.shortcuts import render, HttpResponse
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    sce = models.TextField()





