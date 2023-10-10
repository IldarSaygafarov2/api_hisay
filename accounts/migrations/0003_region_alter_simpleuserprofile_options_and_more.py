# Generated by Django 4.2.5 on 2023-10-10 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_simpleuserprofile_phone_number_and_more'),
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
        migrations.AlterModelOptions(
            name='simpleuserprofile',
            options={'verbose_name': 'Пользователь приложения', 'verbose_name_plural': 'Пользователи приложения'},
        ),
        migrations.AddField(
            model_name='simpleuserprofile',
            name='education',
            field=models.TextField(blank=True, null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='simpleuserprofile',
            name='info_about',
            field=models.TextField(blank=True, null=True, verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='simpleuserprofile',
            name='rating',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Рейтинг сервиса'),
        ),
        migrations.AddField(
            model_name='simpleuserprofile',
            name='service_photo_certificate',
            field=models.ImageField(blank=True, null=True, upload_to='services/certificates/', verbose_name='Фото сертификата сервиса'),
        ),
        migrations.AddField(
            model_name='simpleuserprofile',
            name='user_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatars/', verbose_name='Фото пользователя'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название города')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='accounts.region')),
            ],
            options={
                'verbose_name': 'Города',
            },
        ),
        migrations.AddField(
            model_name='simpleuserprofile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='accounts.city'),
        ),
    ]
