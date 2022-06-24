import time

from django.core.mail import send_mail
from django.test import TestCase
from contact.forms import ContactForm


# Create your tests here.
from techtuneup import settings


class SendContactFormTests(TestCase):
    def test_form_validation(self):
        form_data = {"email": "autotest@email.com", "name": "Tester Bot", "message": "This is a tester email"}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_send_email(self):
        email_subject = 'Test Subject'
        email_message = 'This is a test'
        self.assertTrue(bool(send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)))

    def test_webgui_form(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import NoSuchElementException

        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000/contact/")
        self.assertIn("Contact", driver.title)

        email_field = driver.find_element(By.ID, 'id_email')
        email_field.send_keys('django-tester@mail.com')
        name_field = driver.find_element(By.ID, 'id_name')
        name_field.send_keys('Django Tester')
        message_field = driver.find_element(By.ID, 'id_message')
        message_field.send_keys('This is an automated test, testing the emailer.')
        submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_btn.send_keys(Keys.RETURN)

        driver.close()