"""
Models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from permissions.models import Profile, Permission


class ApiUser(AbstractUser):
    """
    Model ApiUser
    """
    
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=255, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    department = models.CharField(_('department'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    phone_number = models.CharField(_('phone number'), max_length=255, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    immediate_boss = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.username}"


class PasswordToken(models.Model):
    """
    Model UserProfile
    """

    key = models.CharField(_('token'), max_length=255, blank=True)
    user_email = models.CharField(_('user email'), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        return name from model
        """
        return str(self.key)


class UserProfile(models.Model):
    """
    Model UserProfile
    """

    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        """
        return name from model
        """
        return str(self.profile.name)


class UserPermission(models.Model):
    """
    Model UserPermission
    """

    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        """
        return name from model
        """
        return str(self.permission.name)

class Turn(models.Model):
    """
    Model Turn
    """

    name = models.CharField(_('name'), max_length=255, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        """
        return name from model
        """
        return str(self.name)


class Department(models.Model):
    """
    Model Turn
    """

    name = models.CharField(_('name'), max_length=255, unique=True)
    general_profile = models.CharField(_('general profile'), max_length=255, blank=True, null=True)
    root_department = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        """
        return name from model
        """
        return str(self.name)


class UserDepartment(models.Model):
    """
    Model UserDepartment
    """

    user = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    manager = models.BooleanField(_('manager'), default=False)

    def __str__(self):
        """
        return name from model
        """
        return '{}-{}'.format(str(self.department.name), str(self.user.username))