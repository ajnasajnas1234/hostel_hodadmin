# Generated by Django 4.2.1 on 2023-06-20 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0006_admission_fee_amount_for_non_concession"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admission_fee",
            name="Amount_for_non_concession",
        ),
    ]
