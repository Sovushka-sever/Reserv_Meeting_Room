from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class UserRoles(models.TextChoices):

    EMPLOYEE = 'employee', 'Сотрудник'
    OFFICE_MANAGER = 'office_manager', 'Офис_менеджер'


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=False,
    )
    username = models.CharField(
        max_length=30,
        unique=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
    )
    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.EMPLOYEE,
    )
    avatar = models.ImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    objects = UserManager()

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.email

    @property
    def is_employee(self):
        return self.role == UserRoles.EMPLOYEE

    @property
    def is_office_manager(self):
        return self.role == UserRoles.OFFICE_MANAGER
