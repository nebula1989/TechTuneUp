from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def repair_services(request):
    return render(request, 'all-services-repair.html')


def pricing_tables(request):
    return render(request, 'pricing-tables.html')


def team(request):
    return render(request, 'team.html')


def register(request):
    return render(request, 'register.html')


def faq(request):
    return render(request, 'faq.html')


def error_404(request):
    return render(request, '404.html')
