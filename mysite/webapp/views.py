from django.shortcuts import render
from .models import Technology

def home(request):
    technologies = Technology.objects.all()
    return render(request, 'home.html', {'technologies': technologies})
