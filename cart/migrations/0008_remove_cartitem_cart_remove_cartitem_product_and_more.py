# Generated by Django 4.2.4 on 2023-09-27 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_cartitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
