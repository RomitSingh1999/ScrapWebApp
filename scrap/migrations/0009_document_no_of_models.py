# Generated by Django 3.0.4 on 2020-07-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0008_auto_20200722_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='No_of_models',
            field=models.IntegerField(default=1),
        ),
    ]
