# Generated by Django 3.1.4 on 2021-02-06 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_auto_20210206_0250"),
    ]

    operations = [
        migrations.RenameField(
            model_name="picture",
            old_name="picture",
            new_name="picture_1",
        ),
        migrations.RemoveField(
            model_name="product",
            name="pictures",
        ),
        migrations.AddField(
            model_name="picture",
            name="picture_2",
            field=models.ImageField(blank=True, null=True, upload_to="picture/"),
        ),
        migrations.AddField(
            model_name="picture",
            name="picture_3",
            field=models.ImageField(blank=True, null=True, upload_to="picture/"),
        ),
        migrations.AddField(
            model_name="picture",
            name="product",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="app.product",
            ),
        ),
        migrations.CreateModel(
            name="Favorite",
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
                (
                    "product",
                    models.ForeignKey(
                        default="1",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default="1",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.user",
                    ),
                ),
            ],
        ),
    ]
