from tortoise import models

from ezymart_by_evoq.app.models.base import AbstractUser


class User(AbstractUser, models.Model):

    def __str__(self):
        return self.email
