# Generated by Django 3.0.7 on 2020-09-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_popular'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='popular',
            new_name='latest_popular',
        ),
        migrations.AddField(
            model_name='post',
            name='mba_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='startup_popular',
            field=models.BooleanField(default=False),
        ),
    ]
