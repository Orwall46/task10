# Generated by Django 4.1.3 on 2022-12-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_alter_cards_data_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='series',
            field=models.CharField(max_length=2, verbose_name='Серия'),
        ),
    ]
