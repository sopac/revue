# Generated by Django 4.0.4 on 2022-05-11 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revue', '0005_alter_building_photo_1_alter_building_photo_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropsagriculture',
            name='location_line',
        ),
        migrations.RemoveField(
            model_name='infrastructureport',
            name='location_line',
        ),
        migrations.RemoveField(
            model_name='livestock',
            name='location_line',
        ),
    ]
