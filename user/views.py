from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from user.models import User

def user_login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    return render(request, 'user/registration/login.html', {'form': form})

def user_logout(request):
    logout(request)


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html', {'section': dashboard})

def register(request):
    user_form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if user_form.is_valid():
            print(user_form.errors)
            print(user_form.cleaned_data)
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            print(user_form.errors, new_user)

            return render(request, 'user/registration/registration_done.html', {'new_user': new_user})

    return render(request, 'user/registration/registration.html', {'user_form': user_form})

def all_user(request):
    user = User.objects.all()
    return render(request, 'user/base.html', {'user': user})
