# Generated by Django 4.2.3 on 2023-07-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_useraddress_address_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address_name',
            field=models.CharField(max_length=50),
        ),
    ]