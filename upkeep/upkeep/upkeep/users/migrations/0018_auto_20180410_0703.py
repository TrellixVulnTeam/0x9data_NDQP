# Generated by Django 2.0.3 on 2018-04-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20180409_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='white_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=155, verbose_name='管理员名')),
                ('white_list', models.CharField(default='', max_length=1000, verbose_name='电话白名单')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='white_list',
        ),
    ]
