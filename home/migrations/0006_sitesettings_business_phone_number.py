# Generated by Django 3.2.9 on 2021-11-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_sitesettings_monthly_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='business_phone_number',
            field=models.CharField(help_text='Your business phone number.', max_length=20, null=True),
        ),
    ]