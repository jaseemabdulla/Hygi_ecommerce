# Generated by Django 4.2.3 on 2023-07-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_colour_productvariant_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.productvariant'),
        ),
    ]
