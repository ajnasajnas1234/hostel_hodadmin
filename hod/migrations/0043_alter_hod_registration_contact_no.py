# Generated by Django 4.2.1 on 2023-07-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0042_remove_hod_registration_office_no_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hod_registration",
            name="Contact_no",
            field=models.IntegerField(null=True),
        ),
    ]
