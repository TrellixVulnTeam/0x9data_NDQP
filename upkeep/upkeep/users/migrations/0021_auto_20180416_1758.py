# Generated by Django 2.0.3 on 2018-04-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_device_last_unix_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='freq',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
