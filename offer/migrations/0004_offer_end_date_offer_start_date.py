# Generated by Django 4.2.4 on 2023-08-14 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_remove_offer_end_date_remove_offer_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='end_date',
            field=models.DateField(default=datetime.date(2024, 12, 25)),
        ),
        migrations.AddField(
            model_name='offer',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 12, 25)),
        ),
    ]
