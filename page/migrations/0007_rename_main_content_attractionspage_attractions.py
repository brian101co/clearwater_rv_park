# Generated by Django 3.2.9 on 2021-11-27 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20211127_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attractionspage',
            old_name='main_content',
            new_name='attractions',
        ),
    ]
