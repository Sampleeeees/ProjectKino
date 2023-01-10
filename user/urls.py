from django.conf.urls import url
from . import views
from django.contrib.auth import login, logout

urlpatterns = [
    url(r'^login/$', views.user_login, name='login_user'),
    url(r'^logout/$', views.user_logout, name='logout_user'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
]