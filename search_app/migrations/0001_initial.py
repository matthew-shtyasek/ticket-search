# Generated by Django 3.2 on 2023-04-10 04:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateTimeField()),
                ('arrive_date', models.DateTimeField()),
                ('train_number', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(4)])),
                ('destination', models.CharField(max_length=32)),
                ('departure', models.CharField(max_length=32)),
                ('cost', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('cost',),
            },
        ),
    ]