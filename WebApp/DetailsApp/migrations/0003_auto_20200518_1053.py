# Generated by Django 3.0.5 on 2020-05-18 05:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DetailsApp', '0002_auto_20200517_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='LastRefreshedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 18, 5, 23, 50, 152778, tzinfo=utc)),
        ),
    ]
