import os
from pprint import pprint

# Google
from google.cloud import recaptchaenterprise_v1
from google.cloud.recaptchaenterprise_v1 import Assessment
from google.api_core import exceptions as google_exceptions

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from techtuneup.settings import RECAPTCHA_KEY
from .forms import ContactForm


def contact_view(request):
    project_id = 'recaptcha-354614'
    recaptcha_site_key = '6Lfyj1QiAAAAAGJ8-iFk22fmSJu8p4gmAdhKBE5E'
    recaptcha_action = 'SUBMIT'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            token = request.POST['g-recaptcha-response']
            create_assessment(project_id, recaptcha_site_key, token, recaptcha_action)
            try:
                form.save()
                email_subject = f'New contact {form.cleaned_data["name"]}: {form.cleaned_data["email"]}'
                email_message = form.cleaned_data['message']
                send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
                messages.success(request, 'Contact Email Sent Successfully!')
                return redirect('index')

            except google_exceptions.InvalidArgument:
                messages.error(request, "Please check the captcha.")
                return redirect('contact')

        else:
            messages.error(request, "Oops something went wrong")

    form = ContactForm()
    context = {
        "title": "Contact",
        "top_banner_name": "Contact",
        'form': form,
        "recaptcha_key": RECAPTCHA_KEY,
    }

    return render(request, 'contact/contact.html', context)


def success_view(request):
    return render(request, 'contact/success.html')


def error_view(request):
    return render(request, 'contact/error.html')


def create_assessment(
        project_id: str, recaptcha_site_key: str, token: str, recaptcha_action: str
) -> Assessment:
    """Create an assessment to analyze the risk of a UI action.
    Args:
        project_id: GCloud Project ID
        recaptcha_site_key: Site key obtained by registering a domain/app to use recaptcha services.
        token: The token obtained from the client on passing the recaptchaSiteKey.
        recaptcha_action: Action name corresponding to the token.

    filename = "/home/bwalters89/UpOnYourLuck/uponyourluck/settings/google_cred.json"
    credentials = service_account.Credentials.from_service_account_file(filename)
    """

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/etc/google_cred.json"

    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()

    # Set the properties of the event to be tracked.
    event = recaptchaenterprise_v1.Event()
    event.site_key = recaptcha_site_key
    event.token = token

    assessment = recaptchaenterprise_v1.Assessment()
    assessment.event = event

    project_name = f"projects/{project_id}"

    # Build the assessment request.
    request = recaptchaenterprise_v1.CreateAssessmentRequest()
    request.assessment = assessment
    request.parent = project_name

    response = client.create_assessment(request)

    # Check if the token is valid.
    if not response.token_properties.valid:
        print(
            "The CreateAssessment call failed because the token was "
            + "invalid for for the following reasons: "
            + str(response.token_properties.invalid_reason)
        )
        return

    # Check if the expected action was executed.
    if response.token_properties.action != recaptcha_action:
        print(
            "The action attribute in your reCAPTCHA tag does"
            + "not match the action you are expecting to score"
        )
        return
    else:
        # Get the risk score and the reason(s)
        # For more information on interpreting the assessment,
        # see: https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment
        for reason in response.risk_analysis.reasons:
            print(reason)
        print(
            "The reCAPTCHA score for this token is: "
            + str(response.risk_analysis.score)
        )
        # Get the assessment name (id). Use this to annotate the assessment.
        assessment_name = client.parse_assessment_path(response.name).get("assessment")
        print(f"Assessment name: {assessment_name}")
    return response
