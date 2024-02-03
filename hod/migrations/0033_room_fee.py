# Generated by Django 4.2.1 on 2023-07-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0032_mess_track_block_name_mess_track_mess_in_count_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room_fee",
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
                ("Month", models.IntegerField(null=True)),
                ("Amount", models.IntegerField(null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
    ]
