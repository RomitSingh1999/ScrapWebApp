# Generated by Django 3.0.4 on 2020-07-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0007_auto_20200721_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='ChromePath',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='ColumnName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='document',
            name='ImagePath',
            field=models.CharField(default='', max_length=50),
        ),
    ]