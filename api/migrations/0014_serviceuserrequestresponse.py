# Generated by Django 4.2.5 on 2023-11-20 10:07

import api.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_simpleuserprofile_city'),
        ('api', '0013_remove_userrequest_price_alter_userrequest_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceUserRequestResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.simpleuserprofile', validators=[api.validators.validate_user_is_service], verbose_name='Сервис')),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userrequest', verbose_name='Заявка пользователя')),
            ],
            options={
                'verbose_name': 'Отклик сервиса',
                'verbose_name_plural': 'Отклики сервиса',
            },
        ),
    ]
