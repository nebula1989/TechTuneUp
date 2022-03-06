from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'welcome/welcome_index.html')


def services(request):
    return render(request, 'welcome/services.html')