from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def homePage(request):
    return render(request, 'main/home.html', {"tutorials":Tutorial.objects.all})

def register(request):
    if request.method == 'POST':
        RegForm = RegistrationForm(request.POST)
        if RegForm.is_valid():
            user = RegForm.save()
            username = RegForm.cleaned_data.get('username')
            messages.success(request, 'New Account Created for {}'.format(username))
            login(request, user)
            messages.info(request, 'You are Logged in as {}'.format(user))
            return redirect('main:homePage')
        else:
            for msg in RegForm.error_messages:
                messages.error(request, '{} form.error_messages[msg]'.format(msg))
    else:
        RegForm = RegistrationForm()
    return render(request, 'main/register.html', {'RegForm':RegForm})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:homePage')
    return render(request, 'main/login.html')
