# Generated by Django 4.2.1 on 2023-06-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hod_student",
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
                ("Student_name", models.CharField(max_length=200, null=True)),
                ("Admission_no", models.CharField(max_length=500, null=True)),
                ("Joining_date", models.DateField(null=True)),
                ("Status", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="expenditure",
            name="Month",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="Vaccancy",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
