# Generated by Django 2.1 on 2018-10-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('code', models.TextField(max_length=450)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
