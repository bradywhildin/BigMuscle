# name: fitnesstracker/urls.py
# purpose: Handles url assignments for fitnesstracker
# date: 5/12/19
# author: Benjamin Woodatch

from django.conf.urls import url
from . import views

app_name = "fitnesspics"

urlpatterns = [
    url(r'^$', views.fitnesstracker_data, name="data"),
    url(r'^create/$', views.picture_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.pictures_detail, name="detail"),
]
