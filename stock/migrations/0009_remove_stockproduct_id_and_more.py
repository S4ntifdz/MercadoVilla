# Generated by Django 4.2.4 on 2023-09-27 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_alter_stockproduct_code_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockproduct',
            name='id',
        ),
        migrations.AlterField(
            model_name='stockproduct',
            name='code_product',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
