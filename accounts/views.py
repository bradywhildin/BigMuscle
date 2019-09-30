# name: accounts/urls.py
# purpose: Handles requests and renders for accounts urls
# date: 4/21/19
# author: Brady Whildin

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Handles creation of new user
def signup_view(request):
    if request.method == 'POST':  # checks if data was sent
        form = UserCreationForm(request.POST)
        if form.is_valid():  # checks if username and password meet requirements
            user = form.save()  # saves user
            login(request, user)  # logs user in after successful sign up
            return redirect('homepage')  # returns user to homepage after successful sign up
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})  # sends user creation form

# Handles login
def login_view(request):
    if request.method == 'POST':  # checks if data was sent
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():  # checks if username and password belongs to existing user
            user = form.get_user()
            login(request, user)  # logs in user
            return redirect('homepage')  # redirects to homepage of site
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})  # sends login form

def logout_view(request):
    if request.method == 'POST':  # checks if data was sent
        logout(request)  # logs out user
        return redirect(request.META['HTTP_REFERER'])  # returns user to the page they were on
