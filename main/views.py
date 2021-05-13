from django.shortcuts import render
from .models import Tutorial

# Create your views here.
def homePage(request):
    return render(request, 'main/home.html', context={"tutorials":Tutorial.objects.all})

