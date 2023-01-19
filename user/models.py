from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

sex_choice = {(None, ''), ('1', 'Чоловік'), ('2', 'Жінка')}
language_choice = {(None, ''), ('1', 'Українська'), ('2', 'Англійська')}

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first_name'), max_length=50, blank=True)
    last_name = models.CharField(_('last_name'), max_length=50, blank=True)
    nickname = models.CharField(_('nickname'), max_length=75, blank=True, unique=True)
    city = models.CharField(_('city'), max_length=50, blank=True)
    address = models.CharField(_('address'), max_length=55, blank=True)
    card_number = models.CharField(_('card_number'), null=True, max_length=16, blank=True)
    phone = models.IntegerField(_('phone'), blank=True, null=True, unique=True)
    language = models.CharField(max_length=50, choices=language_choice ,blank=True, null=True)
    sex = models.CharField(max_length=50, choices=sex_choice, blank=True, null=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    day_reg = models.DateTimeField(_("date_joined"), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELD = ['nickname']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_active
    #
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)