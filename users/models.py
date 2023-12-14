from django.contrib.auth.models import AbstractUser
from django.db import models


USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class User(AbstractUser):
    roles = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
    )
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    role = models.CharField(
        'Роль пользователя',
        choices=roles,
        max_length=max(len(role[1]) for role in roles), default=USER
    )

    def __str__(self):
        return str(self.username)

    @property
    def is_admin(self):
        return self.role == "admin" or self.is_superuser

    @property
    def is_user(self):
        return self.role == "user"
