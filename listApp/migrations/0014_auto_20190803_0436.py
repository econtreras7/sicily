# Generated by Django 2.2 on 2019-08-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0013_auto_20190502_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='propertyType',
            field=models.CharField(default='Property Type', max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(default='Title', max_length=100),
        ),
    ]
