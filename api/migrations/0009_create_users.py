import datetime

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_users(apps, schema_editor):
	User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
	User.objects.create(
		email='venia@gmail.com',
		first_name='Вениамин',
		last_name='Зайцев',
		position='Инженер',
		experience=2,
		education="Полное высшее",
		patronymic="Петрович",
		date_of_birth=datetime.date(2000, 10, 10),
		password=make_password('123'),
		is_staff=False,
		is_superuser=False
	)
	User.objects.create(
		email='soniy@gmail.com',
		first_name='Софья',
		last_name='Гончарова',
		position='Аналитик',
		experience=10,
		education="Полное высшее",
		patronymic="Олеговна",
		date_of_birth=datetime.date(2000, 9, 2),
		password=make_password('123'),
		is_staff=False,
		is_superuser=False
	)
	User.objects.create(
		email='masha@gmail.com',
		first_name='Мария',
		last_name='Устинова',
		position='Электрик',
		experience=5,
		education="Неполное высшее",
		patronymic="Кирилловна",
		date_of_birth=datetime.date(1988, 7, 3),
		password=make_password('123'),
		is_staff=False,
		is_superuser=False
	)
	User.objects.create(
		email='stas@gmail.com',
		first_name='Стас',
		last_name='Остриков',
		position='Монтажник',
		experience=3,
		education="Неполное высшее",
		patronymic="Владимирович",
		date_of_birth=datetime.date(1998, 3, 3),
		password=make_password('123'),
		is_staff=False,
		is_superuser=False
	)


class Migration(migrations.Migration):
	dependencies = [
		('api', '0008_create_digital_categories'),
	]

	operations = [
		migrations.RunPython(create_users),
	]
