# Generated by Django 4.2.3 on 2023-07-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productvariant_colour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='colour',
            new_name='material',
        ),
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.AddField(
            model_name='image',
            name='product_variant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.productvariant'),
        ),
    ]
