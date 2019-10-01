# name: articles/urls.py
# purpose: Handles url assignments for articles
# date: 4/22/19
# author: Nizom Djuraev

from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create', views.article_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),  # uses user submitted slug to find picture url
]
