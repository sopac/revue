# Generated by Django 4.0.4 on 2022-05-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revue', '0009_alter_building_population_disability'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
