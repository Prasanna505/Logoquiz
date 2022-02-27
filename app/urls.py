from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from app import urls, views
from django.conf.urls.static import static 
# from django.urls import url
from django.views.static import serve


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_user),
    path('logout',views.logout_user),
    path('register',views.register),
    path('home',views.home),
    path('check',views.verify),
    path('leaderboard',views.leaderboard),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)