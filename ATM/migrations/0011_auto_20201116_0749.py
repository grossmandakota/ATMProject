# Generated by Django 3.1.3 on 2020-11-16 12:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0010_auto_20201116_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 16, 7, 49, 52, 644248)),
        ),
    ]
