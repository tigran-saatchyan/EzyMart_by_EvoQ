from tortoise import fields, models

from ezymart_by_evoq.app.helpers.constants import NULLABLE
from ezymart_by_evoq.app.validators.email_validatior import EmailValidator


class AbstractBaseModel(models.Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class AbstractUser(AbstractBaseModel, models.Model):
    email = fields.CharField(
        unique=True,
        max_length=255,
        validators=[EmailValidator]
    )
    password = fields.CharField(max_length=128)
    last_login = fields.DatetimeField(**NULLABLE)

    first_name = fields.CharField(max_length=150, **NULLABLE)
    last_name = fields.CharField(max_length=150, **NULLABLE)
    is_staff = fields.BooleanField(
        default=False,
    )
    is_active = fields.BooleanField(
        default=True,
    )

    telephone = fields.CharField(
        max_length=50,
    )
    telegram_user_id = fields.IntField()
    country = fields.CharField(
        max_length=50,
        **NULLABLE
    )
    city = fields.CharField(
        max_length=50,
        **NULLABLE
    )

    class Meta:
        abstract = True
