# Generated by Django 3.1.4 on 2021-02-06 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_auto_20210206_0308"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="user",
        ),
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="app.address",
            ),
        ),
    ]
