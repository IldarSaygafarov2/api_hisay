# Generated by Django 4.2.5 on 2023-10-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_userrequest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userrequest",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="requests/photos/", verbose_name="Фото"
            ),
        ),
    ]
