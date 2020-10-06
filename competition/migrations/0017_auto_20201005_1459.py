# Generated by Django 3.0.7 on 2020-10-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0016_auto_20201004_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='about',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='competition',
            name='organiser_email',
            field=models.CharField(default='Enter Organiser Email', max_length=50),
        ),
        migrations.AlterField(
            model_name='competition',
            name='organiser_name',
            field=models.CharField(default='Enter Organiser Name', max_length=50),
        ),
    ]