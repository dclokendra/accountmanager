# Generated by Django 3.0.2 on 2020-02-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0004_auto_20200211_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='income/'),
        ),
    ]
