# Generated by Django 3.2.8 on 2021-11-20 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('placemento_app', '0002_hr_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hr_signup',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='hr_signup',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
