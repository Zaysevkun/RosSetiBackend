# Generated by Django 3.1.3 on 2020-11-28 02:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_create_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='request',
            name='authors',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='request',
            name='digital_categories',
            field=models.ManyToManyField(blank=True, to='api.DigitalCategory', verbose_name='Цифровые Категории'),
        ),
        migrations.AlterField(
            model_name='request',
            name='expenses',
            field=models.ManyToManyField(blank=True, to='api.Expenses', verbose_name='Статьи расходов'),
        ),
        migrations.AlterField(
            model_name='request',
            name='rewards',
            field=models.ManyToManyField(blank=True, to='api.Reward'),
        ),
        migrations.AlterField(
            model_name='request',
            name='stages',
            field=models.ManyToManyField(blank=True, to='api.Stage', verbose_name='Этапы'),
        ),
    ]