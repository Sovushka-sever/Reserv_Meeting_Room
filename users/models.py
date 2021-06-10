from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):

    EMPLOYEE = 'employee', 'Employee'
    OFFICE_MANAGER = 'office_manager', 'Office_manager'


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
    """
    This is custom class for create User model.
    """
    email = models.EmailField(
        unique=True,
        verbose_name='email address',
    )
    username = models.CharField(
        max_length=30,
        unique=True
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='personal information',
    )
    role = models.CharField(
        max_length=15,
        choices=UserRoles.choices,
        default=UserRoles.EMPLOYEE,
        verbose_name='user role',
    )
    avatar = models.ImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True,
        verbose_name='user photo',
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.email

    @property
    def is_employee(self):
        """
        Function for quick change property 'role' of User model.
        """
        return self.role == UserRoles.EMPLOYEE

    @property
    def is_office_manager(self):
        """
        Function for quick change property 'role' of User model.
        """
        return self.role == UserRoles.OFFICE_MANAGER

    def get_full_name(self):
        """
        Function for concatenate full name of user, use first and last name.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
