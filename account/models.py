from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email,first_name=None,last_name=None, contact_no=None, password=None):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(
            email=self.normalize_email(email),
            contact_no=contact_no,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name=None,last_name=None, contact_no=None, password=None):
        user = self.create_user(email,first_name,last_name, contact_no, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Enter Your Email",
        unique=True
    )
    contact_no = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    first_name = models.CharField(verbose_name="First Name",max_length=100,null=True)
    last_name = models.CharField(verbose_name="Last Name",max_length=100,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    objects = AccountManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, onj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin
