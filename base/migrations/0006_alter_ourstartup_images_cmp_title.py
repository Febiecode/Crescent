# Generated by Django 3.2.4 on 2023-06-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_ourstartup_images_special_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourstartup_images',
            name='Cmp_title',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
