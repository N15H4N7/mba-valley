# Generated by Django 3.0.7 on 2020-09-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_competition_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]