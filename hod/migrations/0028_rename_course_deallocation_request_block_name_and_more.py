# Generated by Django 4.2.1 on 2023-07-04 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0027_alter_hod_registration_contact_no_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deallocation_request",
            old_name="Course",
            new_name="Block_name",
        ),
        migrations.RemoveField(
            model_name="deallocation_request",
            name="Admission_no",
        ),
        migrations.RemoveField(
            model_name="deallocation_request",
            name="course_name",
        ),
        migrations.AddField(
            model_name="deallocation_request",
            name="Department_name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="deallocation_request",
            name="Room_number",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="deallocation_request",
            name="block",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="hod.block"
            ),
        ),
        migrations.AddField(
            model_name="deallocation_request",
            name="dpt",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hod.department",
            ),
        ),
        migrations.AddField(
            model_name="deallocation_request",
            name="room",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="hod.room"
            ),
        ),
    ]
