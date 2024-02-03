# Generated by Django 4.2.1 on 2023-07-03 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hod", "0023_hod_student_hod"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hod_student",
            name="hod",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
