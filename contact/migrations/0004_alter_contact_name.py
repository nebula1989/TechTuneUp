# Generated by Django 4.0.2 on 2022-06-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
