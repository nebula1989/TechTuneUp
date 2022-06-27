from django.forms import ModelForm
from .models import Contact
from captcha.fields import ReCaptchaField


class ContactForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
