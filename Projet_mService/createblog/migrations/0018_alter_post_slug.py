# Generated by Django 5.0.4 on 2024-04-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createblog', '0017_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
