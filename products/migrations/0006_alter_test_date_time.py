# Generated by Django 4.2.3 on 2023-07-25 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_test_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 4, 8, 32, 433428)),
        ),
    ]
