# Generated by Django 4.2.4 on 2023-08-29 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0004_stockproduct_remove_stock_product_user'),
        ('cart', '0007_alter_cartitem_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='stock_product',
        ),
        migrations.AddField(
            model_name='stockproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
