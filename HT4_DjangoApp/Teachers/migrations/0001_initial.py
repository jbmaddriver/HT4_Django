# Generated by Django 4.2.5 on 2023-09-13 10:12

import Teachers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('science_field', models.CharField(max_length=100)),
                ('science_degree', models.IntegerField()),
                ('groups_number_id', models.CharField(max_length=20, validators=[Teachers.models.validate_comma_separated_integer_list])),
            ],
        ),
    ]
