from tortoise import models, fields

from ezymart_by_evoq.app.models.base import AbstractBaseModel


class Cart(AbstractBaseModel, models.Model):
    product = fields.ForeignKeyField(
        model_name="models.Product",
        related_name="product",
        on_delete=fields.CASCADE
    )
    quantity = fields.IntField(default=1)
    is_active = fields.BooleanField(default=True)
    order = fields.ForeignKeyField(
        model_name="models.Order",
        related_name="cart",
        on_delete=fields.CASCADE
    )
    owner = fields.ForeignKeyField(
        model_name='models.User',
        related_name='cart'
    )

# TODO: add last price to track price changes
# TODO: add folowing fields:
#   is_published,
#   image,
#   category,
#   views_count,
#   current_version,
