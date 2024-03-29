# Generated by Django 4.2.1 on 2023-07-25 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hod", "0040_room_rent_month_transient_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room_registration",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hostelmanagment_room_registrations",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
