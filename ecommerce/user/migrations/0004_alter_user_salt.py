# Generated by Django 4.1.6 on 2023-12-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_alter_user_salt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="salt",
            field=models.CharField(default="Zc7JRAeHhU6w", max_length=12),
        ),
    ]
