# name: fitnesstracker/views.py
# purpose: Handles requests and renders for fitnesstracker
# date: 6/3/19
# author: Benjamin Woodatch, Brady Whildin

from django.shortcuts import render, redirect
from . models import FitnessPic
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse

def fitnesstracker_data(request):
    fitnesspic = FitnessPic.objects.all().order_by("date")
    return render(request, 'fitnesstracker/fitnesstracker_data.html', {'fitnesspic': fitnesspic})

def pictures_detail(request, slug):
    fitnesspic = FitnessPic.objects.get(slug=slug)
    return render(request, 'fitnesstracker/fitnesstracker_detail.html', {'fitnesspic': fitnesspic})

@login_required(login_url='/accounts/login/')
def picture_create(request):  # authenticated login is required for this page
    if request.method == 'POST':  # post means that data was sent
        form = forms.CreatePicture(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('fitnesspics:data')
    else:
        form = forms.CreatePicture()
    return render(request, 'fitnesstracker/fitnesstracker_create.html', {'form': form})
