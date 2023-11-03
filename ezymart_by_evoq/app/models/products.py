from tortoise import models, fields

from ezymart_by_evoq.app.models.base import (
    AbstractBaseModel,
)


class Product(AbstractBaseModel, models.Model):
    name = fields.CharField(max_length=150)
    description = fields.TextField()
    price = fields.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    is_active = fields.BooleanField(default=False)
    owner = fields.ForeignKeyField(
        model_name='models.User',
        related_name='product'
    )

    def __str__(self):
        return self.name

