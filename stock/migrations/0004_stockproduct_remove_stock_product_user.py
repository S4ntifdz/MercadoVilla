# Generated by Django 4.2.4 on 2023-08-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_rename_quantity_stock_product_quantity_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_line', models.CharField(choices=[('Jardineria', 'Jardineria'), ('Ferreteria', 'Ferreteria'), ('Almacen', 'Almacen'), ('Tecnologia', 'Tecnologia'), ('Otros', 'Otros')], default='Otros', max_length=128)),
                ('quantity_stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name_product', models.CharField(max_length=140)),
                ('description', models.TextField(max_length=1200)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('code_product', models.CharField(max_length=10, unique=True)),
                ('expiration', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stock_product',
            name='user',
        ),
    ]
