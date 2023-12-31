# Generated by Django 4.2.5 on 2023-10-10 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_region_city'),
        ('accounts', '0003_region_alter_simpleuserprofile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleuserprofile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cities', to='api.city'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
