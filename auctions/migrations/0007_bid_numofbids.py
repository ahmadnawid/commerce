# Generated by Django 3.1.3 on 2023-01-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_bid_numofbids'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='numofbids',
            field=models.IntegerField(null=True),
        ),
    ]