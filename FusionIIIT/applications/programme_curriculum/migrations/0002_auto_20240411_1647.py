# Generated by Django 3.1.5 on 2024-04-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme_curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='year',
            field=models.PositiveIntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='programme',
            name='programme_begin_year',
            field=models.PositiveIntegerField(default=2024),
        ),
    ]
