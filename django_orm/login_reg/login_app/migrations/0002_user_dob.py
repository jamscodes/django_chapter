# Generated by Django 2.2 on 2020-08-16 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]