from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    context = {
        "top_banner_name": "About",
    }
    return render(request, 'about.html', context)


def repair_services(request):
    context = {
        "top_banner_name": "Repair Services",
    }
    return render(request, 'all-services-repair.html', context)


def tech_services(request):
    context = {
        "top_banner_name": "Technology Services",
    }
    return render(request, 'all-services-technology.html', context)


def laptop_repair(request):
    context = {
        "top_banner_name": "Laptop Repair",
    }
    return render(request, 'laptop-repair.html', context)


def pricing_tables(request):
    context = {
        "top_banner_name": "Prices",
    }
    return render(request, 'pricing-tables.html', context)


def team(request):
    context = {
        "top_banner_name": "Meet the Team",
    }
    return render(request, 'team.html', context)


def register(request):
    context = {
        "top_banner_name": "Sign Up",
    }
    return render(request, 'register.html', context)


def login(request):
    context = {
        "top_banner_name": "Login",
    }
    return render(request, 'login.html', context)


def faq(request):
    context = {
        "top_banner_name": "FAQ",
    }
    return render(request, 'faq.html', context)


def error_404(request):
    return render(request, '404.html')
