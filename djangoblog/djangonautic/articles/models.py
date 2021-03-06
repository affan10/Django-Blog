from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Article(models.Model):
    slug   = models.SlugField(unique=True)
    body   = models.TextField()
    date   = models.DateTimeField(auto_now_add=True)
    title  = models.CharField(max_length=100)
    thumb  = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + '...'