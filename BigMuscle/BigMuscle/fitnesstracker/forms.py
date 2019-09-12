# name: fitnesstracker/forms.py
# purpose: Includes CreatePicture class
# date: 6/3/19
# author: Brady Whildin

from django import forms
from . import models

class CreatePicture(forms.ModelForm):
    class Meta:
        model = models.FitnessPic
        fields = ['title', 'body', 'slug', 'thumb']