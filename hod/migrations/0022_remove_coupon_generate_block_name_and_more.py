# Generated by Django 4.2.1 on 2023-07-03 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0021_remove_coupon_generate_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coupon_generate",
            name="Block_name",
        ),
        migrations.RemoveField(
            model_name="coupon_generate",
            name="Paid_status",
        ),
        migrations.RemoveField(
            model_name="coupon_generate",
            name="block",
        ),
    ]
