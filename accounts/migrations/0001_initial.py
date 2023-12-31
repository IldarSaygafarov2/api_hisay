# Generated by Django 4.2.5 on 2023-09-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_username', models.CharField(blank=True, max_length=150, null=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('tg_chat_id', models.BigIntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('is_service', models.BooleanField(default=False, null=True)),
                ('verification_code', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
    ]
