# Generated by Django 3.0.3 on 2020-02-15 09:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200215_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 9, 8, 30, 53977, tzinfo=utc)),
        ),
    ]
