# Generated by Django 2.2 on 2020-07-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_ninja'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='no desc'),
            preserve_default=False,
        ),
    ]
