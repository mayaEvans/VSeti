from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email,
        full_name, and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, password, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            email, password, **extra_fields
        )


class UserLevel(models.IntegerChoices):
    BASE = 1, 'base'
    ADVANCED = 2, 'advanced'
    EXTRA = 3, 'extra'
    NULL = 4, 'test not passed'


class User(AbstractBaseUser, PermissionsMixin):
    user_platform = [
        (1, 'iOS'),
        (2, 'Android')
    ]
    email = models.EmailField(
        max_length=256,
        unique=True,
        verbose_name='Почта'
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Фамилия'
    )
    patronymic = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='Отчество'
    )
    level = models.IntegerField(
        choices=UserLevel.choices,
        default=UserLevel.NULL,
        blank=True,
        verbose_name='Уровень'
    )
    platform = models.IntegerField(
        choices=user_platform,
        default=1,
        blank=True,
        verbose_name='Платформа'
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='День рождения'
    )
    social_networks = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Социальные сети'
    )
    photo = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )
    city = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name='Город'
    )
    last_login = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата посещения сайта'
    )
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False,
                                       verbose_name='Администратор')
    is_staff = models.BooleanField(default=False,
                                   verbose_name='Сотрудник')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # Метод для отображения в админ панели
    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser
    #
    # def has_module_perms(self, app_label):
    #     return self.is_superuser

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = 'Пользователь'
