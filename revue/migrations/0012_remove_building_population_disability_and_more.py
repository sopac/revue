# Generated by Django 4.0.5 on 2022-06-07 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revue', '0011_building_building_name_building_building_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='population_disability',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_employment_status',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_language',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_number_of_female',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_number_of_males',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_number_of_people_in_the_household',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_place_of_residence',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_telecommunication_access',
        ),
        migrations.RemoveField(
            model_name='building',
            name='population_vehicle',
        ),
    ]