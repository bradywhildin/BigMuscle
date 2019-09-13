# name: fitnesstracker/models.py
# purpose: Includes FitnesssPic class
# date: 5/12/19
# author: Benjamin Woodatch

from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

class FitnessPic(models.Model):
    title = models.CharField(max_length = 15)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)

    def __str__(self):
        return self.title

    def partial(self):
        return self.body[:40] + '...'


