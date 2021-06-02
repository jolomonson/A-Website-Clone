from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def homePage(request):
    return render(request, 'main/home.html', {"tutorials":Tutorial.objects.all})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:homePage')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request, 'main/register.html', {'form':form})

def login(request):
    return render(request, 'main/login.html')
