from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as utxt_lazy
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(utxt_lazy('email address'), unique=True)
    first_name = models.CharField(utxt_lazy('first name'), max_length=32, blank=True)
    last_name = models.CharField(utxt_lazy('last name'), max_length=32, blank=True)
    date_joined = models.DateTimeField(utxt_lazy('date joined'), auto_now_add=True)
    is_active = models.BooleanField(utxt_lazy('active'), default=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = utxt_lazy('user')
        verbose_name_plural = utxt_lazy('users')

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def get_short_name(self):
        return self.first_name

    def send_user_email(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
