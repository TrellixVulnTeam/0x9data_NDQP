# Generated by Django 2.0.3 on 2018-04-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20180410_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='last_unix_time',
            field=models.IntegerField(default=0, verbose_name='最后操作时间'),
        ),
    ]
