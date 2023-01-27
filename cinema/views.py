import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from adminlte.models import *
from django.views.generic.base import View
from user.models import User
from user.forms import UserRegistrationForm
# Create your views here.


def cabinet(request):
    print(request.user.id)
    user = User.objects.get(pk=request.user.id)
    form = UserRegistrationForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
    return render(request, 'cinema/usercabinet.html', {'form': form})


def page_info(request, page_id):
    page = Page.objects.get(pk=page_id)
    gallery_list = Image.objects.filter(gallery=page.gallery.id)

    context = {
        'page': page,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/newpage.html', context)

def index(request):
    today = timezone.datetime.today()
    speed = SpeedCarousel.objects.get(pk=1)
    speed2 = SpeedCarousel.objects.get(pk=2)
    banner_list = TopHomeBanner.objects.all
    film = Film.objects.all()
    news = NewsAndDiscountBanner.objects.all()
    context = {'banner_list': banner_list, 'film_list': film, 'news_banner': news, 'speed': speed, 'speed2': speed2, 'today': today}
    return render(request, 'cinema/index.html', context)


def soon(request):
    film = Film.objects.all()
    today = timezone.datetime.today()

    context = {
        'film_list': film,
        'today': today
    }
    return render(request, 'cinema/soon.html', context)

def timetable(request):
    date = datetime.date.today()
    weeks = date + datetime.timedelta(days=6)
    cinema_list = Cinema.objects.all()
    film_list = Film.objects.all()
    hall_list = Hall.objects.all()
    session = Session.objects.all().order_by('day', 'time_start')
    date_all = session.filter(day__gte=date, day__lte=weeks).distinct('day')
    print(date_all)

    context = {
        'session': session,
        'cinema_list': cinema_list,
        'film_list': film_list,
        'hall_list': hall_list,
        'date_all': date_all,
        'today': date,
        'week': weeks
    }
    return render(request, 'cinema/timetable.html', context)

def cinema(request):
    cinema = Cinema.objects.all()

    context = {
        'cinema_list': cinema
    }
    return render(request, 'cinema/cinema.html', context)

def cinemainfo(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    hall = Hall.objects.filter(cinema=cinema.id)
    print(hall.all())
    gallery_list = Image.objects.filter(gallery=cinema.gallery.id)
    print(gallery_list.all())
    context = {
        'cinema': cinema,
        'gallery_list': gallery_list,
        'hall_list': hall
    }
    return render(request, 'cinema/cinema_info.html', context)

def discount(request):
    discount_list = NewsAndDiscount.objects.filter(type='Discount')
    print(discount_list.all())

    context = {
        'discount_list': discount_list
    }
    return render(request, 'cinema/discount.html', context)

def discount_info(request, dis_id):
    discount = NewsAndDiscount.objects.get(type='Discount', pk=dis_id)
    gallery_list =Image.objects.filter(gallery=discount.gallery.id)

    context={
        'discount':discount,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/discount_info.html', context)

def newss(request):
    news_list = NewsAndDiscount.objects.filter(type='News')

    context = {
        'news_list': news_list
    }
    return render(request, 'cinema/newss.html', context)

def news_info(request, news_id):
    news = NewsAndDiscount.objects.get(type='News', pk=news_id)
    gallery_list = Image.objects.filter(gallery=news.gallery.id)

    context = {
        'news': news,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/news_info.html', context)

def advertising(request):
    adv = Page.objects.get(namepage='Advert')
    gallery_list = Image.objects.filter(gallery=adv.gallery.id)

    context = {
        'advert': adv,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/advertising.html', context)

def viphall(request):
    viphall = Page.objects.get(namepage='VipHall')
    gallery_list = Image.objects.filter(gallery=viphall.gallery.id)


    context = {
        'viphall': viphall,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/viphall.html', context)

def childroom(request):
    child = Page.objects.get(namepage='Childroom')
    gallery_list = Image.objects.filter(gallery=child.gallery.id)

    context = {
        'child': child,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/childroom.html', context)

def cafebar(request):
    cafebar = Page.objects.get(namepage='Cafe-bar')
    gallery_list = Image.objects.filter(gallery=cafebar.gallery.id)

    context = {
        'cafebar': cafebar,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/cafebar.html', context)

def mobileapp(request):
    return render(request, 'cinema/mobileapp.html')

def contacts(request):
    contact = Contact.objects.all()


    context = {
        'contact_list': contact
    }
    return render(request, 'cinema/contacts.html', context)

def cinemaabout(request):
    cinema = Page.objects.get(namepage='About Cinema')
    gallery_list = Image.objects.filter(gallery=cinema.gallery.id)


    context = {
        'cinema': cinema,
        'gallery_list': gallery_list
    }
    return render(request, 'cinema/aboutcinema.html', context)

def auth(request):
    return render(request, 'cinema/auth.html')

class AfishaView(View):
    def get(self, request):
        film = Film.objects.all()
        today = timezone.datetime.today()

        return render(request, 'cinema/afisha.html', {'film_list': film, 'today': today})

class FilmDetailView(View):
    def get(self, request, pk):
        film = Film.objects.get(id=pk)

        return render(request, 'cinema/filmdetail.html', {'film': film})



