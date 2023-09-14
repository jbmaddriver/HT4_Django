# Generated by Django 4.2.5 on 2023-09-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('group_level', models.CharField(max_length=20)),
                ('date_star', models.DateField()),
                ('duration', models.DurationField()),
                ('number_of_students', models.IntegerField()),
                ('average_mark', models.FloatField()),
            ],
        ),
    ]
