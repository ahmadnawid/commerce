# Generated by Django 3.1.3 on 2023-01-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='numofbids',
            field=models.IntegerField(null=True),
        ),
    ]
