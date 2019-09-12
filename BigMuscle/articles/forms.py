# name: articles/forms.py
# purpose: Includes CreateArticle class
# date: 6/2/19
# author: Brady Whildin

from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug']