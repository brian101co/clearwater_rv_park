# Generated by Django 3.2.9 on 2021-11-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_sitesettings_business_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='address',
            field=models.TextField(help_text='Your business address.', null=True),
        ),
    ]
