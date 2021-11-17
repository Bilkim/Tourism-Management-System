from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

"""
class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, last_name, password1, password2, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
           raise ValueError(
                'Superuser must be assigned to is_superuser = True.')

        return self.create_user(email, username, first_name, last_name, password1, password2, **other_fields)




    def create_user(self, email, username, first_name,last_name, password1, password2, **other_fields):
            if not email:
                raise ValueError(gettext_lazy('You must provide an email address'))

            email = self.normalize_email(email)
            user = self.model(email=email, username=username, first_name=first_name,
                               last_name=last_name, password1=password1, password2 = password2, **other_fields)
            
            user.set_password(password2)
            user.save()
            return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy('email address'),unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name', 'password1','password2']

    def __str__(self):
        return self.user_name


"""


