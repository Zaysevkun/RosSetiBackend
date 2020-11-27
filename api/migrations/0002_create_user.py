from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_users(apps, schema_editor):
	User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
	User.objects.create(
		email='andrey@gmail.com',
		first_name='Андрей',
		last_name='Денисов',
		position='Инженер',
		experience=1,
		password=make_password('123'),
		is_staff=False,
		is_superuser=False
	)
	User.objects.create(
		email='kirill@gmail.com',
		first_name='Кирилл',
		last_name='Ильичев',
		position='Админ',
		password=make_password('123'),
		is_staff=True,
		is_superuser=True
	)


class Migration(migrations.Migration):
	dependencies = [
		('api', '0001_initial'),
	]

	operations = [
		migrations.RunPython(create_users),
	]
