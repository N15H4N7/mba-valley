# Generated by Django 3.0.7 on 2020-10-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0014_competition_team_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]