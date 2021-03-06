# Generated by Django 3.1.4 on 2021-02-06 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_auto_20210206_0322"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.citie"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.countrie",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="region",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.region"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="address",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name="Address",
        ),
    ]
