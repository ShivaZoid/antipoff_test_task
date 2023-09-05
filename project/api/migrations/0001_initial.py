# Generated by Django 4.2.4 on 2023-09-05 04:37

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastre_number', models.CharField(max_length=19, unique=True, validators=[api.validators.validate_cadastre_number])),
                ('latitude', models.FloatField(validators=[api.validators.validate_latitude])),
                ('longitude', models.FloatField(validators=[api.validators.validate_longitude])),
                ('response', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
