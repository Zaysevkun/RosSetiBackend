# Generated by Django 3.1.3 on 2020-11-28 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20201128_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
