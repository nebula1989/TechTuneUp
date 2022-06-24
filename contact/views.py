from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["name"]}: {form.cleaned_data["email"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            messages.success(request, 'Contact Email Sent Successfully!')
            return redirect('index')
        else:
            messages.error(request, "Oops something went wrong")
    form = ContactForm()
    context = {
        "title": "Contact",
        "top_banner_name": "Contact",
        'form': form
    }

    return render(request, 'contact/contact.html', context)


def success_view(request):
    return render(request, 'contact/success.html')
