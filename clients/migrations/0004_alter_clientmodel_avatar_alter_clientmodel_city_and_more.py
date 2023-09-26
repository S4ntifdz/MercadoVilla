# Generated by Django 4.2.4 on 2023-09-25 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_rename_imagen_clientmodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientmodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='city',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='postal_code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='clientmodel',
            name='state',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
