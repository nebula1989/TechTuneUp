from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    context = {
        "top_banner_name": "About",
    }
    return render(request, 'about.html', context)


def all_services(request):
    context = {
        "top_banner_name": "All Services",
    }
    return render(request, 'all-services.html', context)


def repair_services(request):
    context = {
        "top_banner_name": "Repair Services",
    }
    return render(request, 'repair-services-base.html', context)


def tech_services(request):
    context = {
        "top_banner_name": "Technology Services",
    }
    return render(request, 'technology-services-base.html', context)


def app_dev(request):
    context = {
        "top_banner_name": "Application Development",
    }
    return render(request, 'development-services-base.html', context)


def pc_repair(request):
    context = {
        "top_banner_name": "PC Repair",
    }
    return render(request, 'pc-repair.html', context)


def mobile_repair(request):
    context = {
        "top_banner_name": "Mobile Repair",
    }
    return render(request, 'mobile-repair.html', context)


def tablet_repair(request):
    context = {
        "top_banner_name": "Tablet Repair",
    }
    return render(request, 'tablet-repair.html', context)


def gaming_repair(request):
    context = {
        "top_banner_name": "Gaming Console Repair",
    }
    return render(request, 'game-console-repair.html', context)


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
    context = {
        "top_banner_name": "404 Page Not Found",
    }
    return render(request, '404.html', context)


