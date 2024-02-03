# Generated by Django 4.2.1 on 2023-06-28 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0014_login_student_log_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessComplaint",
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
                ("Date", models.DateField(null=True)),
                ("Complaint_description", models.CharField(max_length=500, null=True)),
                (
                    "Reply",
                    models.CharField(default="no reply", max_length=500, null=True),
                ),
                ("Title", models.CharField(max_length=500, null=True)),
                ("Block_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "Student_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("Status", models.CharField(max_length=100)),
                (
                    "block",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.block",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hod.student",
                    ),
                ),
            ],
        ),
    ]
