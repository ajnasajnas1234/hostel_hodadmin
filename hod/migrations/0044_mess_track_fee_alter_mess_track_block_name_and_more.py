# Generated by Django 4.2.1 on 2023-07-27 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hod", "0043_alter_hod_registration_contact_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="mess_track",
            name="Fee",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Block_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Date",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Department_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="In_or_out",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Mess_in_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Mess_in_date",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Mess_out_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Mess_out_date",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Month",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Status",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Student_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Students_present",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="Time",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="mess_track",
            name="block",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hod.block",
            ),
        ),
        migrations.DeleteModel(
            name="Mess_fee",
        ),
    ]
