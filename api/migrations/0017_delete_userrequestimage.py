# Generated by Django 4.2.5 on 2024-01-23 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_userrequestimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRequestImage',
        ),
    ]