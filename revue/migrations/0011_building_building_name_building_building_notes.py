# Generated by Django 4.0.5 on 2022-06-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revue', '0010_building_lat_building_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='building_notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]