# Generated by Django 4.2.3 on 2023-07-24 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_order_payment_mode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_mode',
            new_name='payment_method',
        ),
    ]
