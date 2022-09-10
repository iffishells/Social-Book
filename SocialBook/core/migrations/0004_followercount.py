# Generated by Django 4.1.1 on 2022-09-10 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_likepost"),
    ]

    operations = [
        migrations.CreateModel(
            name="FollowerCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("follower", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=500)),
            ],
        ),
    ]
