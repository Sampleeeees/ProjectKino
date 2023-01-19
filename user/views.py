from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .authenticate import EmailAuthBackend

def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'user/registration/registration_done.html', {'new_user': new_user})
    context = {'form': form}
    return render(request, 'user/registration/registration.html', context)

def login_user(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        user = EmailAuthBackend.authenticate(request, nickname=cd['nickname'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                user_ident = EmailAuthBackend.get_user(request, user_id=user.id)
                return render(request, 'user/registration/login_done.html', {'user_name': user, 'user': user_ident})
            else:
                return HttpResponse('Disabled account')
        else:
            form = LoginForm(request.POST or None)
            return render(request, 'user/registration/login_error.html', {'form': form})
    context = {'form': form}
    return render(request, 'user/registration/login.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')
