from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from adminlte.models import Image, SeoBlock, Gallery, Film
from django.views.generic.base import View
from user.models import User
from user.forms import UserRegistrationForm
# Create your views here.

def base(request):
    if request.user.is_authenticated:
        user_active = request.user

    context = {'user': user_active}
    return render(request, 'cinema/base.html', context)

def cabinet(request):
    print(request.user.id)
    user = User.objects.get(pk=request.user.id)
    form = UserRegistrationForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
    return render(request, 'cinema/usercabinet.html', {'form': form})

def index(request):
    return render(request, 'cinema/index.html')


def soon(request):
    return render(request, 'cinema/soon.html')

def timetable(request):
    return render(request, 'cinema/timetable.html')

def cinema(request):
    return render(request, 'cinema/cinema.html')

def discount(request):
    return render(request, 'cinema/discount.html')

def newss(request):
    return render(request, 'cinema/newss.html')

def advertising(request):
    return render(request, 'cinema/advertising.html')

def viphall(request):
    return render(request, 'cinema/viphall.html')

def childroom(request):
    return render(request, 'cinema/childroom.html')

def cafebar(request):
    return render(request, 'cinema/cafebar.html')

def mobileapp(request):
    return render(request, 'cinema/mobileapp.html')

def contacts(request):
    return render(request, 'cinema/contacts.html')

def auth(request):
    return render(request, 'cinema/auth.html')

class AfishaView(View):
    def get(self, request):
        film = Film.objects.all()

        return render(request, 'cinema/afisha.html', {'film_list': film})

class FilmDetailView(View):
    def get(self, request, pk):
        film = Film.objects.get(id=pk)

        return render(request, 'cinema/filmdetail.html', {'film': film})

