# Generated by Django 4.1.3 on 2022-12-06 09:03

import cards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='data_end',
            field=models.DateTimeField(default=cards.models.gen_time, verbose_name='Дата окончания'),
        ),
    ]
