# Generated by Django 2.2.15 on 2020-08-21 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghost', '0004_ghostpost_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='votes',
        ),
    ]
