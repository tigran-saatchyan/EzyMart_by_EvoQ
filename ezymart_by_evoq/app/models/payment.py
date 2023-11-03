from tortoise import models, fields

from ezymart_by_evoq.app.helpers.constants import NULLABLE
from ezymart_by_evoq.app.models.base import AbstractBaseModel


class Payment(AbstractBaseModel, models.Model):
    """
    Model representing a payment.

    This model represents a payment made by a user for a course or a lesson.
    It includes fields for the user
    making the payment, payment date, associated course or lesson, payment
    amount, and payment type.

    Attributes:

        payment_date (DateTimeField): The date and time when the payment was
        paid_amount (decimal): The amount paid for the course or lesson.
        payment_method (str): The type of payment, chosen from predefined
        choices.

    Methods:
        __str__(): Returns a string representation of the payment, including
        the user and associated course/lesson.

    Usage:
        - Use this model to represent payments made by users in your Django
        application.
    """

    PAYMENT_METHOD_CASH = 'cash'
    PAYMENT_METHOD_CARD = 'card'
    PAYMENT_METHOD_TRANSFER_TO_ACCOUNT = 'transfer_to_account'

    PAYMENT_METHODS = (
        (PAYMENT_METHOD_CASH, 'Cash'),
        (PAYMENT_METHOD_CARD, 'Card'),
        (PAYMENT_METHOD_TRANSFER_TO_ACCOUNT, 'Transfer to account'),
    )

    payment_date = fields.DatetimeField(
        auto_now_add=True
    )

    paid_amount = fields.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = fields.CharField(
        max_length=50,
        choices=PAYMENT_METHODS,
    )
    order = fields.ForeignKeyField(
        model_name='models.Order',
        related_name='payment'
    )
    owner = fields.ForeignKeyField(
        model_name='models.User',
        related_name='payment'
    )

    def __str__(self):
        return f'{self.order} - {self.payment_method}'
