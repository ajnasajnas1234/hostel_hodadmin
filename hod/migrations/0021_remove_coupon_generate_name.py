# Generated by Django 4.2.1 on 2023-07-03 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0020_alter_student_room_no"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="coupon_generate",
            name="Name",
        ),
    ]