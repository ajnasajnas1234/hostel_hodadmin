# Generated by Django 4.2.1 on 2023-07-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0030_rename_room_no_room_rent_block_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="Student_name",
            field=models.CharField(max_length=200),
        ),
    ]
