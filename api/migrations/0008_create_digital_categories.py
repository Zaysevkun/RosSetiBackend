from django.db import migrations


def create_users(apps, schema_editor):
	DigitalCategory = apps.get_model('api', 'DigitalCategory')
	DigitalCategory.objects.create(
		name="Управление технологическим процессом"
	)
	DigitalCategory.objects.create(
		name="Дополнительные сервисы"
	)
	DigitalCategory.objects.create(
		name="Цифровая сеть"
	)
	DigitalCategory.objects.create(
		name="Цифровое управление компанией"
	)
	DigitalCategory.objects.create(
		name="Комплексная система информационной безопасности"
	)


class Migration(migrations.Migration):
	dependencies = [
		('api', '0007_auto_20201127_2249'),
	]
	
	operations = [
		migrations.RunPython(create_users),
	]
