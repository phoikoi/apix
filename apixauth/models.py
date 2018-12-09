from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class ApixUserManager(UserManager):
    pass

class ApixUser(AbstractUser):
    objects = ApixUserManager()

    @property
    def friendly_name(self):
        names = " ".join((self.first_name, self.last_name)).strip()
        if len(names)==0:
            return self.username
        else:
            return names

