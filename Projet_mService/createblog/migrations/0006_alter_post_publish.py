# Generated by Django 5.0.4 on 2024-04-15 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createblog', '0005_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 15, 5, 35, 17, 321762, tzinfo=datetime.timezone.utc)),
        ),
    ]
