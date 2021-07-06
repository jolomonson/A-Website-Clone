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
def deeplearningneuralnetworks(request):
    return render(request, 'main/tutorials/MachineLearning/deep-learning-neural-networks/index.html')
def cloudgpus(request):
    return render(request, 'main/tutorials/MachineLearning/cloud-gpus/index.html')
def reinforcementlearning(request):
    return render(request, 'main/tutorials/MachineLearning/reinforcement-learning/index.html')
def selfdrivingcars(request):
    return render(request, 'main/tutorials/MachineLearning/self-driving-cars/index.html')
def deeplearningwithtensorflowkeras(request):
    return render(request, 'main/tutorials/MachineLearning/deep-learning-tensorflow-keras/index.html')
def practicalmachinelearning(request):
    return render(request, 'main/tutorials/MachineLearning/practical-machine-learning/index.html')
def gtav(request):
    return render(request, 'main/tutorials/MachineLearning/gta-v/index.html')
def chatbotwithdeeplearning(request):
    return render(request, 'main/tutorials/MachineLearning/chatbot-with-deep-learning/index.html')
def unconventionalneuralnetworks(request):
    return render(request, 'main/tutorials/MachineLearning/unconventional-neural-networks/index.html')
def tensorflowjs(request):
    return render(request, 'main/tutorials/MachineLearning/tensorflowjs/index.html')
def tensorflowobjectdetection(request):
    return render(request, 'main/tutorials/MachineLearning/tensorflow-object-detection/index.html')
def supportvectormachines(request):
    return render(request, 'main/tutorials/MachineLearning/support-vector-machines/index.html')
def learnaboutclustering(request):
    return render(request, 'main/tutorials/MachineLearning/learn-about-clustering/index.html')







def starcraftiiai(request):
    return render(request, 'main/tutorials/MachineLearning/starcraft-ii-ai/index.html')
def haliteiiartificialintelligence(request):
    return render(request, 'main/tutorials/MachineLearning/halite-ii-ai/index.html')
def imagerecognition(request):
    return render(request, 'main/tutorials/MachineLearning/image-recognition/index.html')




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