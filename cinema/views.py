import datetime
import json

import faker
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    cinema = request.GET.get('cinema_select')
    print(cinema)

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
        fake = faker.Faker('RU_ru')
        data_for_film = {
            'year': fake.year(),
            'country': fake.country(),
            'director': fake.name(),
            'writer': fake.name(),
            'producer': fake.name(),
            'actor': fake.name(),
            'cinema': fake.name()
        }

        return render(request, 'cinema/filmdetail.html', {'film': film, 'data_film': data_for_film})


def cinema_filter(request):
    response = request.GET.get('id_cinema')
    print(response)
    if response == '0':
        current_cinema = serializers.serialize('json', Cinema.objects.all())
        halls = serializers.serialize('json', Hall.objects.all())
        session = serializers.serialize('json', Session.objects.all())
        films = serializers.serialize('json', Film.objects.all())
        return JsonResponse({'cinema': current_cinema, 'halls': halls, 'session': session, 'films': films}, status=200)
    else:
        cinema = Cinema.objects.filter(pk=response)
        print(cinema)
        current_cinema = serializers.serialize('json', cinema)
        halls = serializers.serialize('json', Hall.objects.filter(cinema=response))
        session = serializers.serialize('json', Session.objects.filter(hall__cinema=cinema.get(pk=response)))
        films = serializers.serialize('json', Film.objects.all())
        return JsonResponse({'cinema': current_cinema, 'halls': halls, 'session': session, 'films': films}, status=200)

def hall_filter(request):
    response_hall = request.GET.get('id_hall')
    print(response_hall)
    if response_hall == '0':
        cinema = Cinema.objects.all()
        sess = Session.objects.all()
        current_hall = serializers.serialize('json', Hall.objects.all())
        current_cinema_for_hall = serializers.serialize('json', Cinema.objects.all())
        all_hall_in_cinema = serializers.serialize('json', Hall.objects.all())
        session = serializers.serialize('json', Session.objects.all())
        films = serializers.serialize('json', Film.objects.all())
        return JsonResponse({'current_hall': current_hall, 'current_cinema': current_cinema_for_hall, 'all_hall': all_hall_in_cinema, 'session': session, 'films':films, 'cinema': cinema}, status=200)

    else:
        hall = Hall.objects.get(pk=response_hall)
        cinema = Cinema.objects.get(pk=hall.cinema.id)
        sess = Session.objects.filter(hall=hall.id)
        current_hall = serializers.serialize('json', Hall.objects.filter(pk=response_hall))
        current_cinema_for_hall = serializers.serialize('json', Cinema.objects.filter(pk=hall.cinema.id))
        all_hall_in_cinema = serializers.serialize('json', Hall.objects.filter(cinema=cinema.id))
        session = serializers.serialize('json', Session.objects.filter(hall=hall.id))
        films = serializers.serialize('json', Film.objects.all())


        return JsonResponse({'current_hall': current_hall, 'current_cinema': current_cinema_for_hall, 'all_hall': all_hall_in_cinema, 'session': session, 'films':films}, status=200)

def film_filter(request):
    film_id = request.GET.get('film_id')
    cinema_id = request.GET.get('cinema_id')
    hall_id = request.GET.get('hall_id')
    film_type = request.GET.get('film_type')
    start_day = request.GET.get('startday')
    end_day = request.GET.get('endday')

    print(film_id, cinema_id, hall_id,  film_type, start_day, end_day)


    if hall_id != '0' and cinema_id != 0:
        hall = serializers.serialize('json', Hall.objects.filter(pk=hall_id))
        cinema = serializers.serialize('json', Cinema.objects.filter(pk=cinema_id))
        film = serializers.serialize('json', Film.objects.filter(pk=film_id))
        session = serializers.serialize('json', Session.objects.filter(film=film_id))
        print(hall)
        return JsonResponse({'hall': hall, 'cinema': cinema, 'film': film, 'session': session}, status=200)
    else:
        hall = serializers.serialize('json', Hall.objects.all())
        cinema = serializers.serialize('json', Cinema.objects.all())
        film = serializers.serialize('json', Film.objects.filter(pk=film_id))
        session = serializers.serialize('json', Session.objects.filter(film=film_id))
        return JsonResponse({'hall': hall, 'cinema': cinema, 'film': film, 'session': session}, status=200)


def booking(request, pk):
    current_session = Session.objects.get(pk=pk)
    current_film_for_session = Film.objects.get(pk=current_session.film.id)
    current_hall_for_session = Hall.objects.get(pk=current_session.hall.id)
    date = datetime.date.today()

    context = {
        'film': current_film_for_session,
        'hall': current_hall_for_session,
        'session': current_session,
        'date': date
    }
    return render(request, 'cinema/booking.html', context=context)

def booking_delete(request):
    id_booking = request.GET.get('id_booking')
    print(id_booking)
    delete_booking = get_object_or_404(Ticket, id=id_booking)
    delete_booking.delete()
    return HttpResponse()

def list_booking(request):
    if request.POST:
        list_place = request.POST.get('list_place')
        instance_place = json.loads(list_place)

        for data in instance_place:
            id = data['id']
            row = data['row']
            place = data['place']
            price = data['price']
            user = request.user.pk
            session_id = data['session_id']
            if request.POST:
                ticket = Ticket()
                ticket.id = id
                ticket.row = row
                ticket.place = place
                ticket.price = price
                ticket.user_id = user
                ticket.session_id = session_id
                ticket.save()
    user = request.user.pk
    session = request.GET.get('session')
    print(session)
    all_user_tickets = Ticket.objects.filter(user_id=user, session_id=session)
    all_tickets = Ticket.objects.filter(session_id=session).exclude(user_id=user)
    ticket_user_data = serializers.serialize('json', all_user_tickets)
    ticket_data = serializers.serialize('json', all_tickets)

    return JsonResponse({'ticket_user_data': ticket_user_data, 'ticket_data': ticket_data}, status=200)