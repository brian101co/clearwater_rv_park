# Generated by Django 3.2.3 on 2021-05-23 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20201004_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='link_anchor',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
