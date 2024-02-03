# Generated by Django 4.2.1 on 2023-06-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0008_admission_fee_amount_for_non_concession"),
    ]

    operations = [
        migrations.AddField(
            model_name="mess_registration",
            name="Password1",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="mess_registration",
            name="Password2",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="mess_registration",
            name="Role",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mess_registration",
            name="Username",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="room_registration",
            name="Password1",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="room_registration",
            name="Password2",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="room_registration",
            name="Role",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room_registration",
            name="Username",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
