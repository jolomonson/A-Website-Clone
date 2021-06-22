from email import message
from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def homePage(request):
    return render(request, 'main/home.html')

def machinelearningtutorials(request):
    return render(request, 'main/tutorials/MachineLearning/machine-learning-tutorials/index.html')

def dataanalysistutorials(request):
    return render(request, 'main/tutorials/DataAnalysis/data-analysis-tutorials/index.html')

def quantumprogrammingtutorials(request):
    return render(request, 'main/tutorials/QuantumProgramming/quantum-programming-tutorials/index.html')

def quantumprogrammingtutorials(request):
    return render(request, 'main/tutorials/QuantumProgramming/quantum-programming-tutorials/index.html')

def gamedevelopmenttutorials(request):
    return render(request, 'main/tutorials/GameDevelopment/game-development-tutorials/index.html')

def pythonfundamentaltutorials(request):
    return render(request, 'main/tutorials/PythonFundamentals/python-fundamental-tutorials/index.html')

def webdevelopmenttutorials(request):
    return render(request, 'main/tutorials/WebDevelopment/web-development-tutorials/index.html')

def bottutorials(request):
    return render(request, 'main/tutorials/Bots/bot-tutorials/index.html')

def roboticstutorials(request):
    return render(request, 'main/tutorials/Robotics/robotics-tutorials/index.html')

def guitutorials(request):
    return render(request, 'main/tutorials/GUI/gui-development-tutorials/index.html')

def golangtutorials(request):
    return render(request, 'main/tutorials/Golang/golang-tutorials/index.html')


def register(request):
    if request.method == 'POST':
        RegForm = RegistrationForm(request.POST)
        if RegForm.is_valid():
            user = RegForm.save()
            username = RegForm.cleaned_data.get('username')
            messages.success(request, 'New Account Created for: {}'.format(username)) 
            login(request, user)
            messages.info(request, 'You are Logged in as {}'.format(user))
            return redirect('main:homePage')
        else:
            for msg in RegForm.error_messages:
                messages.error(request, '{} form.error_messages[msg]'.format(msg))
    else:
        RegForm = RegistrationForm
    return render(request, 'main/register.html', {'RegForm':RegForm})

def user_login(request):
    if request.method == 'POST':
        LoginForm = AuthenticationForm(request, data=request.POST)
        if LoginForm.is_valid():
            username = LoginForm.cleaned_data.get('username')
            password = LoginForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are Logged in as {}'.format(username))
                return redirect('main:homePage')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Username or Password is Incorrect')
    LoginForm = AuthenticationForm()
    return render(request, 'main/login.html', {'LoginForm':LoginForm})

def user_logout(request):
    logout(request)
    return redirect('/')