# Generated by Django 2.2.1 on 2020-04-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0002_auto_20200430_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='abv',
            field=models.FloatField(default=6),
        ),
        migrations.AddField(
            model_name='beer',
            name='ibu',
            field=models.FloatField(default=70),
        ),
    ]