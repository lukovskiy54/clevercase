# Generated by Django 4.2.8 on 2023-12-06 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0015_merge_20231206_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 6, 15, 7, 4, 12787)),
        ),
        migrations.AlterField(
            model_name='othersdebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 6, 15, 7, 4, 13850)),
        ),
    ]