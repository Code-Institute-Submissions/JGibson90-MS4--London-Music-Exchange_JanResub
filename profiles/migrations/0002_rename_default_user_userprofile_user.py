# Generated by Django 3.2.6 on 2021-09-24 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_user',
            new_name='user',
        ),
    ]