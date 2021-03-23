# Generated by Django 3.1.4 on 2021-02-05 22:49

import app.views
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="picture",
            name="picture1",
        ),
        migrations.RemoveField(
            model_name="picture",
            name="picture2",
        ),
        migrations.RemoveField(
            model_name="picture",
            name="picture3",
        ),
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="postal_code",
        ),
        migrations.RemoveField(
            model_name="user",
            name="products",
        ),
        migrations.AddField(
            model_name="picture",
            name="picture",
            field=models.ImageField(
                blank=True, null=True, upload_to=app.models.Picture.generate_filename
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 2, 5, 23, 49, 17, 198692),
                editable=False,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="user",
            field=models.ForeignKey(
                default="1", on_delete=django.db.models.deletion.CASCADE, to="app.user"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 2, 5, 23, 49, 17, 197194),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="categorie",
            name="name",
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(default=10, null=True),
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=100, null=True)),
                ("phone_number", models.IntegerField(null=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.citie"
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.countrie"
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.region"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="state",
            field=models.ForeignKey(
                default="1", on_delete=django.db.models.deletion.CASCADE, to="app.state"
            ),
        ),
    ]