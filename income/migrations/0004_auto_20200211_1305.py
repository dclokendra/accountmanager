# Generated by Django 3.0.2 on 2020-02-11 07:20

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0003_auto_20200211_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]