"""TutorialsWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homePage, name='home'),path('home/', views.homePage, name='homePage'),
    path('machine-learning-tutorials/', views.machinelearningtutorials, name='machineLearning'),
    path('data-analysis-tutorials/', views.dataanalysistutorials, name='dataAnalysis'),
    path('quantum-programming-tutorials/', views.quantumprogrammingtutorials, name='quantumProgramming'),
    path('game-development-tutorials/', views.gamedevelopmenttutorials, name='gameDevelopment'),
    path('python-fundamental-tutorials/', views.pythonfundamentaltutorials, name='pythonFundamentals'),
    path('web-development-tutorials/', views.webdevelopmenttutorials, name='webDevelopment'),
    path('bot-tutorials/', views.bottutorials, name='botandai'),
    path('robotics-tutorials/', views.roboticstutorials, name='robotics'),
    path('gui-development-tutorials/', views.guitutorials, name='gui'),
    path('golang-tutorials/', views.golangtutorials, name='golang'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
