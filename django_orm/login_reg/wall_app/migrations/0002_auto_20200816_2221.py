# Generated by Django 2.2 on 2020-08-17 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Message',
            new_name='message',
        ),
    ]