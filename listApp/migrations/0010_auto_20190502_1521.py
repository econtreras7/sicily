# Generated by Django 2.2 on 2019-05-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0009_auto_20190502_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='propertyStatus',
            field=models.CharField(choices=[('For Sale', 'For Sale'), ('Pending Sale', 'Pending Sale'), ('Sold', 'Sold')], default='For Sale', max_length=10),
        ),
    ]
