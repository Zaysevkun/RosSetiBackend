# Generated by Django 3.1.3 on 2020-11-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_merge_20201128_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='author_id',
            field=models.PositiveSmallIntegerField(default=3, verbose_name='id автора сообщения'),
            preserve_default=False,
        ),
    ]
