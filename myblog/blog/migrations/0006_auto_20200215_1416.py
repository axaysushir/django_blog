# Generated by Django 3.0.3 on 2020-02-15 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200215_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 8, 46, 30, 409651, tzinfo=utc)),
        ),
    ]
