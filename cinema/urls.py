from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('afisha/', views.AfishaView.as_view(), name='afisha'),
    path('afisha/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('soon/', views.soon, name='soon'),
    path('timetable/', views.timetable, name='timetable'),
    path('cinema/', views.cinema, name='cinema'),
    path('discount/', views.discount, name='discount'),
    path('news/', views.newss, name='newss'),
    path('advertising/', views.advertising, name='advertising'),
    path('viphall/', views.viphall, name='viphall'),
    path('childroom/', views.childroom, name='childroom'),
    path('cafebar/', views.cafebar, name='cafebar'),
    path('mobileapp/', views.mobileapp, name='mobileapp'),
    path('contacts/', views.contacts, name='contacts'),
    path('usercabinet/', views.cabinet, name='cabinet'),
]