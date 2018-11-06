# Generated by Django 2.1.1 on 2018-10-03 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Share', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='code',
        ),
        migrations.AddField(
            model_name='code',
            name='source_code',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='code',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 3, 17, 43, 0, 85198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='code',
            name='title',
            field=models.CharField(default=' ', max_length=250),
        ),
    ]
