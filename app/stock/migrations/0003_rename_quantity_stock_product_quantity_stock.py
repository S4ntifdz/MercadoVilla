# Generated by Django 4.2.4 on 2023-08-21 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_product_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_product',
            old_name='quantity',
            new_name='quantity_stock',
        ),
    ]