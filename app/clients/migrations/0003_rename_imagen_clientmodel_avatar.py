# Generated by Django 4.2.4 on 2023-08-21 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_clientmodel_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientmodel',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
