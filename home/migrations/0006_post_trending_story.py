# Generated by Django 3.0.7 on 2020-09-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200922_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='trending_story',
            field=models.BooleanField(default=True),
        ),
    ]
