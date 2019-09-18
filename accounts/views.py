# name: accounts/urls.py
# purpose: Handles requests and renders for accounts urls
# date: 4/21/19
# author: Brady Whildin

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Handles creation of new user
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # gives sign up ability to signup.html
        if form.is_valid():
            user = form.save()
            login(request, user)  # logs user in after successful sign up
            return redirect('homepage')  # returns user to homepage after successful sign up
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(request.META['HTTP_REFERER'])