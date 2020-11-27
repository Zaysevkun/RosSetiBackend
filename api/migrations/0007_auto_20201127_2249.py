# Generated by Django 3.1.3 on 2020-11-27 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_comment_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Статья расходов')),
                ('cost', models.PositiveBigIntegerField(verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('count_of_days', models.PositiveIntegerField(verbose_name='Кол-во дней')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.question', verbose_name='вопрос комментария'),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Процент')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата вознаграждения')),
                ('is_signature', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='Заголовок')),
                ('is_digital_categories', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('characteristic', models.TextField(blank=True, null=True, verbose_name='Характеристика')),
                ('expectations', models.TextField(blank=True, null=True, verbose_name='Ожидание')),
                ('is_saving_money', models.BooleanField(default=False)),
                ('authors', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Авторы')),
                ('digital_categories', models.ManyToManyField(blank=True, null=True, to='api.DigitalCategory', verbose_name='Цифровые Категории')),
                ('expenses', models.ManyToManyField(blank=True, null=True, to='api.Expenses', verbose_name='Статьи расходов')),
                ('rewards', models.ManyToManyField(blank=True, null=True, to='api.Reward')),
                ('stages', models.ManyToManyField(blank=True, null=True, to='api.Stage', verbose_name='Этапы')),
            ],
        ),
    ]