# Generated by Django 4.1.6 on 2023-10-09 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0004_alter_user_created_at_alter_user_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 9, 15, 52, 25, 26078, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 10, 9, 15, 52, 25, 26212, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]