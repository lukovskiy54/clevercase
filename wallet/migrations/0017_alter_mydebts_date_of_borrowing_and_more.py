# Generated by Django 4.2.8 on 2023-12-06 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0016_alter_mydebts_date_of_borrowing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 7, 0, 7, 18, 498867)),
        ),
        migrations.AlterField(
            model_name='othersdebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 7, 0, 7, 18, 499862)),
        ),
    ]