from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Define a model manager for User model with no username set
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Custom User Class
class User(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)
    patronymic = models.CharField('Отчество', max_length=100)
    position = models.CharField('Должность', max_length=100)
    department = models.CharField('Подразделение', max_length=100, blank=True, null=True)
    date_of_birth = models.DateField("Дата рождения", blank=True, null=True)
    education = models.CharField("Образование", max_length=100, blank=True, null=True)
    experience = models.PositiveIntegerField("Стаж", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.email}"

    @property
    def full_name(self):
        first_name = getattr(self, 'first_name', '')
        last_name = getattr(self, 'last_name', '')
        return f"{first_name} {last_name}".strip()


# class