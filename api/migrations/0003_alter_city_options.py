# Generated by Django 4.2.5 on 2023-10-10 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_region_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
    ]
