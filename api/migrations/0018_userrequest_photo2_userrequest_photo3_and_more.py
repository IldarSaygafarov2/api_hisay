# Generated by Django 4.2.5 on 2024-01-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_delete_userrequestimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 2'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 3'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 4'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 5'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 6'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 7'),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='requests/photos/', verbose_name='Фото 8'),
        ),
    ]