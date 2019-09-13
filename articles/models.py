# name: articles/models.py
# purpose: Includes Article class
# date: 4/22/19
# author: Nizom Djuraev

from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)

    def __str__(self):
        return self.title


