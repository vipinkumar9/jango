# Generated by Django 4.0.3 on 2022-03-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_issue_sprint_issue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='issue_id',
            new_name='issue',
        ),
    ]