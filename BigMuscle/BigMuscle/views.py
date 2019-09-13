# name: fitnesstracker/views.py
# purpose: Handles requests and renders for homepage
# date: 6/3/19
# author: Brady Whildin


from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html')


def logInCreateAccount(request):
    return render(request, 'LogInCreateAccount.html')