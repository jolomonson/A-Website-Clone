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
# Machine Learning
def machinelearningtutorials(request):
    return render(request, 'main/tutorials/MachineLearning/machine-learning/index.html')
def deeplearningneuralnetworks(request):
    return render(request, 'main/tutorials/MachineLearning/neural-networks/index.html')
def cloudgpus(request):
    return render(request, 'main/tutorials/MachineLearning/cloud-gpus/index.html')
def reinforcementlearning(request):
    return render(request, 'main/tutorials/MachineLearning/reinforcement/index.html')
def selfdrivingcars(request):
    return render(request, 'main/tutorials/MachineLearning/self-driving-cars/index.html')
def deeplearningwithtensorflowkeras(request):
    return render(request, 'main/tutorials/MachineLearning/tensorflow-keras/index.html')
def practicalmachinelearning(request):
    return render(request, 'main/tutorials/MachineLearning/practical-ml/index.html')
def gtav(request):
    return render(request, 'main/tutorials/MachineLearning/gta-v/index.html')
def starcraftiiai(request):
    return render(request, 'main/tutorials/MachineLearning/starcraft-ii-ai/index.html')
def chatbotwithdeeplearning(request):
    return render(request, 'main/tutorials/MachineLearning/chatbot/index.html')
def unconventionalneuralnetworks(request):
    return render(request, 'main/tutorials/MachineLearning/unconventional-net/index.html')
def tensorflowjs(request):
    return render(request, 'main/tutorials/MachineLearning/tensorflowjs/index.html')
def tensorflowobjectdetection(request):
    return render(request, 'main/tutorials/MachineLearning/tensorflow-object/index.html')
def supportvectormachines(request):
    return render(request, 'main/tutorials/MachineLearning/svm/index.html')
def learnaboutclustering(request):
    return render(request, 'main/tutorials/MachineLearning/clustering/index.html')  
def imagerecognition(request):
    return render(request, 'main/tutorials/MachineLearning/image-recognition/index.html')
def haliteiiartificialintelligence(request):
    return render(request, 'main/tutorials/MachineLearning/halite-ii-ai/index.html')
# Data Analysis
def dataanalysistutorials(request):
    return render(request, 'main/tutorials/DataAnalysis/data-analysis/index.html')
def machinelearning(request):
    return render(request, 'main/tutorials/DataAnalysis/machine-learning/index.html')
def dataanalysiswithpandas(request):
    return render(request, 'main/tutorials/DataAnalysis/da-pandas/index.html')
def datavisualizationwithdashandpython(request):
    return render(request, 'main/tutorials/DataAnalysis/dv-dash/index.html')
def datavisualization(request):
    return render(request, 'main/tutorials/DataAnalysis/visualization/index.html')
def finance(request):
    return render(request, 'main/tutorials/DataAnalysis/finance/index.html')
def stockprices(request):
    return render(request, 'main/tutorials/DataAnalysis/finance/stock-prices/index.html')
def sklearnintro(request):
    return render(request, 'main/tutorials/DataAnalysis/finance/sklearn-intro/index.html')
def googlecloud(request):
    return render(request, 'main/tutorials/DataAnalysis/google-cloud/index.html')
def imagesandvideoanalysis(request):
    return render(request, 'main/tutorials/DataAnalysis/image-analysis/index.html')
def distributedcomputing(request):
    return render(request, 'main/tutorials/DataAnalysis/distributed-computing/index.html')
def naturallanguageprocessing(request):
    return render(request, 'main/tutorials/DataAnalysis/nl-processing/index.html')
#Quantum Programming
def quantumprogrammingtutorials(request):
    return render(request, 'main/tutorials/QuantumProgramming/qp-tutorials/index.html')
#Game Development
def gamedevelopmenttutorials(request):
    return render(request, 'main/tutorials/GameDevelopment/game-development/index.html')
#Python Fundamentals
def pythonfundamentaltutorials(request):
    return render(request, 'main/tutorials/PythonFundamentals/python-funds/index.html')
def pythonbasics(request):
    return render(request, 'main/tutorials/PythonFundamentals/basics/index.html')
def pythonintermediate(request):
    return render(request, 'main/tutorials/PythonFundamentals/intermediate/index.html')
def socketstutorial(request):
    return render(request, 'main/tutorials/PythonFundamentals/socket-tutorials/index.html')
#Web Development
def webdevelopmenttutorials(request):
    return render(request, 'main/tutorials/WebDevelopment/web-dev/index.html')
def djangowebdevelopment(request):
    return render(request, 'main/tutorials/WebDevelopment/web-dev/django/index.html')
def flask(request):
    return render(request, 'main/tutorials/WebDevelopment/web-dev/flask/index.html')
#Bots and AI
def bottutorials(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/index.html')
def gtav(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/gta-v/index.html')
def redditapiwrapper(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/reddit-api/index.html')
def selfdrivingcars(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/sd-cars/index.html')
def discordbots(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/discord-bots/index.html')
def beautifulsouptutorial(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/bs4/index.html')
def starcraftiiai(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/starcraft-ii/index.html')
def haliteiiartificialintelligence(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/halite-ii/index.html')
def haliteiiiartificialintelligence(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/halite-iii/index.html')
def alexaskills(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/alexa-skills/index.html')
def twitterapi(request):
    return render(request, 'main/tutorials/BotsandAI/bot-tutorials/twitter-api/index.html')
    #Robotics
def raspberrypi(request):
    return render(request, 'main/tutorials/Robotics/robotics-tutorials/raspberry/index.html')
def roboticsraspberrypi(request):
    return render(request, 'main/tutorials/Robotics/robotics-tutorials/bots-pi/index.html')
def buildingquadcopter(request):
    return render(request, 'main/tutorials/Robotics/robotics-tutorials/quad/index.html')
def roboticstutorials(request):
    return render(request, 'main/tutorials/Robotics/robotics-tutorials/index.html')
    #GUI
def guitutorials(request):
    return render(request, 'main/tutorials/GUI/gui-tutorials/index.html')
def pyqt(request):
    return render(request, 'main/tutorials/GUI/gui-tutorials/gui-pyqt/index.html')
def tkinter(request):
    return render(request, 'main/tutorials/GUI/gui-tutorials/tkinter/index.html')
def kivy(request):
    return render(request, 'main/tutorials/GUI/gui-tutorials/kivy/index.html')
#Golang
def golangtutorials(request):
    return render(request, 'main/tutorials/Golang/golang-tutorials/index.html')
def syntaxgolanguage(request):
    return render(request, 'main/tutorials/Golang/golang-tutorials/syntax-go/index.html')



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