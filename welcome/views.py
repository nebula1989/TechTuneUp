from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def repair_services(request):
    return render(request, 'all-services-repair.html')


def error_404(request):
    return render(request, '404.html')
