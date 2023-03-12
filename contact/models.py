from django.db import models
import datetime


class Contact(models.Model):
    email = models.EmailField(max_length=75, unique=True)
    name = models.CharField(max_length=100, default="")
    message = models.TextField()
    date_sent = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Contact'
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
