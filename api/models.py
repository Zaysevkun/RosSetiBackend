from django.contrib.auth import get_user_model
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
    phone = models.CharField("Номер телефона", max_length=32, blank=True, null=True)

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


class Chat(models.Model):
    title = models.CharField('название чата', max_length=12)
    user1 = models.ForeignKey(User, verbose_name='первый пользователь в чате', on_delete=models.CASCADE,
                              related_name='user1')
    user2 = models.ForeignKey(User, verbose_name='второй пользователь в чате', on_delete=models.CASCADE,
                              related_name='user2')


class Category(models.Model):
    name = models.TextField('Название категории')
    description = models.TextField('описание')

    class Meta:
        verbose_name = 'Категория форума'
        verbose_name_plural = 'Категории форума'

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField('краткий вопрос', max_length=64)
    description = models.TextField('развернутый вопрос')
    author = models.ForeignKey(User, verbose_name='автор вопроса', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='категория вопроса',
                                 on_delete=models.CASCADE,
                                 related_name='questions')
    ask_date = models.DateTimeField('Когда задан вопрос', auto_now=True)

    class Meta:
        verbose_name = 'Вопроc форума'
        verbose_name_plural = 'Вопросы форума'

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField('текст комментария')
    author = models.ForeignKey(User, verbose_name='автор комментария', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='вопрос комментария',
                                 on_delete=models.CASCADE,
                                 related_name='comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.pk


class DigitalCategory(models.Model):
    name = models.TextField("Название")


class Expenses(models.Model):
    name = models.TextField("Статья расходов")
    cost = models.PositiveBigIntegerField("Стоимость")


class Stage(models.Model):
    name = models.TextField("Название")
    count_of_days = models.PositiveIntegerField("Кол-во дней")


class Reward(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="Автор", on_delete=models.CASCADE)
    percentage = models.PositiveSmallIntegerField("Процент", blank=True, null=True)
    date = models.DateField("Дата вознаграждения", blank=True, null=True)
    is_signature = models.BooleanField(default=False)


class RequestComment(models.Model):
    FIELD_NAME_CHOICES = [
        ('title', 'title'),
        ('digital_categories', 'digital_categories'),
        ('description', 'description'),
        ('characteristic', 'characteristic'),
        ('expenses', 'expenses'),
        ('stages', 'stages'),
        ('expectations', 'expectations'),
        ('authors', 'authors'),
        ('rewards', 'rewards'),
    ]
    field_name = models.CharField("Название поля", max_length=256, choices=FIELD_NAME_CHOICES)
    comment = models.TextField()
    author = models.ForeignKey(
        get_user_model(), verbose_name="Автор", blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Request(models.Model):
    title = models.TextField("Заголовок", blank=True, null=True)
    is_digital_categories = models.BooleanField(default=False)
    digital_categories = models.ManyToManyField(
        DigitalCategory, verbose_name='Цифровые Категории', blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    characteristic = models.TextField("Характеристика", blank=True, null=True)
    expenses = models.ManyToManyField(
        Expenses, verbose_name="Статьи расходов", blank=True, null=True)
    stages = models.ManyToManyField(Stage, verbose_name="Этапы", blank=True, null=True)
    expectations = models.TextField("Ожидание", blank=True, null=True)
    authors = models.ManyToManyField(get_user_model(), verbose_name="Авторы", blank=True, null=True)
    rewards = models.ManyToManyField(Reward, blank=True, null=True)
    is_saving_money = models.BooleanField(default=False)
    comments = models.ManyToManyField(RequestComment, verbose_name="Комментарии", blank=True)
    created_by = models.ForeignKey(get_user_model(), models.CASCADE, related_name='requests',
                                   verbose_name='Кем создана', blank=True, null=True)
    created_at = models.DateField('Создано', auto_now_add=True, blank=True, null=True)
    status = models.TextField('Статус', blank=True, null=True)
    is_draft = models.BooleanField("Черновик?", default=True)

    class Meta:
        ordering = ['-created_at']


class Messages(models.Model):
    text = models.TextField('текст сообщения')
    time = models.DateTimeField('время сообщения', auto_now=True)
    chat = models.ForeignKey(Chat, verbose_name='чат', on_delete=models.CASCADE, related_name='messages')

