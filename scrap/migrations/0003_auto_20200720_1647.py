# Generated by Django 3.0.4 on 2020-07-20 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_register_user_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='registers',
        ),
    ]
