from fastapi import HTTPException
from tortoise import models, fields

from ezymart_by_evoq.service.base_model import (
    BaseDateCreatedModifiedModel,
    AbstractBaseModel,
)
from ezymart_by_evoq.service.constants import NULLABLE
from ezymart_by_evoq.users.utils import hash_password, compare_passwords
from ezymart_by_evoq.users.validatiors import EmailValidator, PasswordValidator


class User(AbstractBaseModel, BaseDateCreatedModifiedModel, models.Model):
    email = fields.CharField(
        unique=True,
        max_length=255,
        validators=[EmailValidator()]
    )
    password = fields.CharField(
        max_length=128,
        validators=[PasswordValidator()]
    )

    first_name = fields.CharField(max_length=150, **NULLABLE)
    last_name = fields.CharField(max_length=150, **NULLABLE)
    telephone = fields.CharField(max_length=50, **NULLABLE)
    telegram_user_id = fields.IntField(**NULLABLE)
    country = fields.CharField(
        max_length=50,
        **NULLABLE
    )
    city = fields.CharField(
        max_length=50,
        **NULLABLE
    )

    last_login = fields.DatetimeField(**NULLABLE)

    is_superuser = fields.BooleanField(default=False)
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)
    is_verified = fields.BooleanField(default=False)

    def __str__(self):
        return self.email

    def verify_password(self, password):
        return compare_passwords(self.password, password)

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.first_name or self.last_name:
            return (f"{self.first_name.title() or ''} "
                    f"{self.last_name.title() or ''}").strip()
        return self.email

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["password"]

    @classmethod
    def create_superuser(cls):
        email = input("Enter email: ")
        password = input("Enter password: ")
        password2 = input("Enter password again: ")
        if password != password2:
            raise HTTPException(
                status_code=400,
                detail="Passwords do not match"
            )

        user = cls(
            email=email,
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        hashed_password = hash_password(password)
        user.password = hashed_password
        user.save()
        print("Superuser created successfully")
        return user
