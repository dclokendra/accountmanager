# Generated by Django 3.0.2 on 2020-02-10 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200210_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
