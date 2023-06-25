from django.shortcuts import render
from .models import City


def index(request):
    projects = City.objects.all()
    return render(request, 'info/index.html', {'projects': projects})

# Create your views here.
