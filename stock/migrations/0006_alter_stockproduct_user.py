# Generated by Django 4.2.4 on 2023-09-17 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0005_delete_stock_product_stockproduct_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproduct',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_seller': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
