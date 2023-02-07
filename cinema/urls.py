from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('afisha/', views.AfishaView.as_view(), name='afisha'),
    path('afisha/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),
    path('soon/', views.soon, name='soon'),
    path('timetable/', views.timetable, name='timetable'),
    path('cinema/', views.cinema, name='cinema'),
    path('cinema/info<cinema_id>', views.cinemainfo, name='cinemainfo'),
    path('discount/', views.discount, name='discount'),
    path('discount/info<dis_id>', views.discount_info, name='discount_info'),
    path('news/', views.newss, name='newss'),
    path('news/info<news_id>', views.news_info, name='news_info'),
    path('page/info<page_id>', views.page_info, name='page_info'),
    path('advertising/', views.advertising, name='advertising'),
    path('viphall/', views.viphall, name='viphall'),
    path('childroom/', views.childroom, name='childroom'),
    path('cafebar/', views.cafebar, name='cafebar'),
    path('aboutcinema/', views.cinemaabout, name='cinemaabout'),
    path('contacts/', views.contacts, name='contacts'),
    path('usercabinet/', views.cabinet, name='cabinet'),
    path('booking/<int:pk>', views.booking, name='booking'),
    path('booking/delete', views.booking_delete, name='booking_delete'),
    path('booking/list_booking', views.list_booking, name='list_booking'),


    path('timetable/cinema_filter', views.cinema_filter, name='cinema_filter'),
    path('timetable/hall_filter', views.hall_filter, name='hall_filter'),
    path('timetable/film_filter', views.film_filter, name='film_filter'),
]