# Generated by Django 4.2.5 on 2023-09-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0002_rename_date_star_groups_list_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups_list',
            name='duration',
            field=models.CharField(max_length=20),
        ),
    ]