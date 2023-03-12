from django.shortcuts import render


def index(request):
    context = {
        "top_banner_name": "Home",
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "top_banner_name": "About",
    }
    return render(request, 'about.html', context)


def services(request):
    context = {
        "top_banner_name": "Services",
    }
    return render(request, 'services.html', context)


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
