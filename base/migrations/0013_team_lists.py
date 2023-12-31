# Generated by Django 4.2.2 on 2023-10-03 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0012_center_of_excellance_key_point1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="team_lists",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("team_name", models.CharField(max_length=200)),
                ("special_at", models.CharField(max_length=200)),
                (
                    "team_img",
                    models.ImageField(
                        default="images/user_image.png",
                        upload_to="teams_profile/%Y/%m/%d",
                    ),
                ),
                ("TECK_OR_NONTECK", models.CharField(max_length=200)),
                (
                    "last_updated_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
