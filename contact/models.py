from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100, default="")
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Contact'
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
