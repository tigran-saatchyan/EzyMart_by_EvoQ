from tortoise import models, fields
from ezymart_by_evoq.models.base_model import (
    AbstractBaseModel,
    BaseDateCreatedModifiedModel,
)


class Product(AbstractBaseModel, BaseDateCreatedModifiedModel, models.Model):
    """
    Represents a product in the application.

    Attributes:
    - name (str): The name of the product (max length 150 characters).
    - description (str): The description of the product.
    - price (decimal): The price of the product with 2 decimal places.
    - is_active (bool): Indicates if the product is currently active (
    default is False).
    - owner (models.User): The owner of the product.

    Methods:
    - __str__(): Returns the name of the product as a string.

    PydanticMeta:
    - exclude (list): Excludes owner, created_at, modified_at, and is_active
    from Pydantic models.
    """
    name = fields.CharField(max_length=150)
    description = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    is_active = fields.BooleanField(default=False)
    owner = fields.ForeignKeyField(
        model_name='models.User', related_name='product'
        )

    # ... (TODO fields and relationships)

    def __str__(self):
        """
        Returns the name of the product as a string.
        """
        return self.name

    class PydanticMeta:
        exclude = ['owner', 'created_at', 'modified_at', 'is_active']

#   TODO: fields and relationships:
#       original_price = fields.DecimalField(max_digits=10, decimal_places=2)
#       new_price = fields.DecimalField(max_digits=10, decimal_places=2)
#       percentage_discount = fields.IntField()
#       offer_expiration_date = fields.DatetimeField(
#           default=datetime.now(),
#           **NULLABLE
#       )
#       product_images = fields.ManyToManyField(
#           'models.ProductImage', related_name='products'
#       )
#       product_category = fields.ForeignKeyField(
#           'models.ProductCategory', related_name='products'
#       )
#       product_tags = fields.ManyToManyField(
#           'models.ProductTag', related_name='products'
#       )
#       product_reviews = fields.ManyToManyField(
#           'models.ProductReview', related_name='products'
#       )
#       product_rating = fields.DecimalField(max_digits=10, decimal_places=2)
#       product_rating_count = fields.IntField()
#       product_rating_sum = fields.IntField()
#       product_views_count = fields.IntField()
#       product_versions = fields.ManyToManyField(
#           'models.ProductVersion', related_name='products'
#       )
#       product_is_published = fields.BooleanField(default=False)
