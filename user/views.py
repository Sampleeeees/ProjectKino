from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

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

def login(request):
    context = {}
    return render(request, 'user/registration/login.html', context)
