# Generated by Django 4.0.2 on 2022-07-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_options_alter_contact_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=75, unique=True),
        ),
    ]
