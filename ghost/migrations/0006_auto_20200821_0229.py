# Generated by Django 2.2.15 on 2020-08-21 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghost', '0005_remove_ghostpost_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ghostpost',
            name='up_votes',
            field=models.IntegerField(default=0),
        ),
    ]
