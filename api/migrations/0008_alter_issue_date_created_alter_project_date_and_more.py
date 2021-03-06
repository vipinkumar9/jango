# Generated by Django 4.0.3 on 2022-03-03 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_issue_date_created_project_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date_created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userissue',
            name='date_assigned',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
