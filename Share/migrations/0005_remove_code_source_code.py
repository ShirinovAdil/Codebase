# Generated by Django 2.1.1 on 2018-10-09 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Share', '0004_personalcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='source_code',
        ),
    ]
