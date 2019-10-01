# name: articles/views.py
# purpose: Handles requests and renders for articles
# date: 6/3/19
# authors: Nizom Djuraev, Brady Whildin

from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')  # orders articles by date posted
    return render(request, 'articles/article_list.html', {'articles': articles})  # renders list of posted articles

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)  # retrieves user submitted slug that will be used to find detail url
    return render(request, 'articles/article_detail.html' ,{'article':article})

@login_required(login_url='/accounts/login/')  # page can only be accessed by logged in user
def article_create(request):
    if request.method == 'POST':  # checks if data was sent
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():  # checks if all fields were filled out
            instance = form.save(commit=False)
            instance.author = request.user  # takes in author's username to use with other article info
            instance.save()
            return redirect('articles:list')  # redirects to list of posted articles
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})  # sends article creation form