# name: accounts/urls.py
# purpose: Handles url assignments
# date: 4/21/19
# author: Brady Whildin

from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings

app_name = 'accounts'  # allows urls starting with accounts/ to be grouped below

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
