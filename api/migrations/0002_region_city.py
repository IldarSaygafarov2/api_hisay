# Generated by Django 4.2.5 on 2023-10-10 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название области или региона')),
            ],
            options={
                'verbose_name': 'Регион/Область',
                'verbose_name_plural': 'Регионы/Области',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название города')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='api.region')),
            ],
            options={
                'verbose_name': 'Города',
            },
        ),
    ]
