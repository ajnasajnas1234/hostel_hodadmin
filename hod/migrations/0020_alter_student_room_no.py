# Generated by Django 4.2.1 on 2023-07-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0019_rename_date_in_mess_in_and_out_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="Room_no",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
