# Generated by Django 4.0.3 on 2022-03-03 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_userissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='date_created',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userissue',
            name='date_assigned',
            field=models.DateField(default=datetime.date.today),
        ),
    ]