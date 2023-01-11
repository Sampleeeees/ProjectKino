from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import login, logout

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]