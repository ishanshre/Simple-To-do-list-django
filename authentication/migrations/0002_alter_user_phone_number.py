# Generated by Django 4.1 on 2022-08-13 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(9000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
