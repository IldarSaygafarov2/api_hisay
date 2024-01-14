# Generated by Django 4.2.5 on 2024-01-09 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_servicesetting_address_by_location_and_more'),
        ('api', '0014_serviceuserrequestresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_requests', to='accounts.simpleuserprofile', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='Описание заявки'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_requests', to='api.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='title',
            field=models.CharField(blank=True, default='', max_length=155, null=True, verbose_name='Заголовок статьи'),
        ),
    ]
