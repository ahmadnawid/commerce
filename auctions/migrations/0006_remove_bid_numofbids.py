# Generated by Django 3.1.3 on 2023-01-25 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20230125_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='numofbids',
        ),
    ]
