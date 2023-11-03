from tortoise import models, fields

from ezymart_by_evoq.app.models.base import AbstractBaseModel


class Order(AbstractBaseModel, models.Model):
    is_paid = fields.BooleanField(default=False)
    products = fields.ManyToManyField(
        model_name="models.Product",
        related_name="products",
        through="order_products",
    )
    owner = fields.ForeignKeyField(
        model_name='models.User',
        related_name='order'
    )