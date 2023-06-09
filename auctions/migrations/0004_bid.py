# Generated by Django 3.1.3 on 2023-01-25 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20230124_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentbid', models.IntegerField()),
                ('numofbids', models.IntegerField()),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_id', to='auctions.listing')),
            ],
        ),
    ]
