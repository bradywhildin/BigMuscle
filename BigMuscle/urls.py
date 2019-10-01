# name: fitnesstracker/urls.py
# purpose: Handles url assignments for all parts of website
# date: 6/4/19
# author: Brady Whildin

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('accounts/', include('accounts.urls')),  # include() allows app's urls to be stored at appname.urls
    path('logInCreateAccount/', views.logInCreateAccount, name='logInCreateAccount'),
    path('fitnesstracker/', include('fitnesstracker.urls')),
    path('articles/', include('articles.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

