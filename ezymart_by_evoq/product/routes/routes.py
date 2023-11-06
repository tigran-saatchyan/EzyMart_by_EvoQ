from fastapi import APIRouter, status, HTTPException

from ezymart_by_evoq.product import schemas
from ezymart_by_evoq.product.models import Product
from ezymart_by_evoq.product.services import is_product_exists

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get(
    "/",
    status_code=status.HTTP_200_OK
)
async def list_products() -> schemas.ProductRetrieveSchema:
    """
    Retrieve a list of products.

    Returns:
        schemas.ProductRetrieveSchema: A schema representing the list of
        products.

    Raises:
        HTTPException: If no products are found, a 404 error is raised.
    """
    data = Product.all()
    product = await schemas.ProductRetrieveSchema.from_queryset(data)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Products not found"
        )
    return product


@products_router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create(
    product_data: schemas.ProductCreateSchema
) -> schemas.ProductRetrieveSchema:
    """
    Create a new product.

    Args:
        product_data (schemas.ProductCreateSchema): The data for the new
        product.

    Returns:
        schemas.ProductRetrieveSchema: A schema representing the created
        product.
    """
    product = await Product.create(
        **product_data.model_dump(exclude_unset=True)
    )
    return await schemas.ProductRetrieveSchema.from_tortoise_orm(product)


@products_router.get(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
)
async def retrieve(product_id: int) -> schemas.ProductRetrieveSchema:
    """
    Retrieve a product by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        schemas.ProductRetrieveSchema: A schema representing the retrieved
        product.

    Raises:
        HTTPException: If the product is not found, a 404 error is raised.
    """
    product = await Product.filter(id=product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product


@products_router.patch(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ProductPartialUpdateSchema
)
async def partial_update(
    product_id: int,
    product_data: schemas.ProductPartialUpdateSchema
) -> schemas.ProductPartialUpdateSchema:
    """
    Partially update a product by its ID.

    Args:
        product_id (int): The ID of the product to update.
        product_data (schemas.ProductPartialUpdateSchema): The data to
        update the product.

    Returns:
        schemas.ProductPartialUpdateSchema: A schema representing the
        partially updated product.
    """
    data = product_data.model_dump(exclude_unset=True)
    await is_product_exists(product_id)

    await Product.filter(id=product_id).update(**data)

    return await schemas.ProductRetrieveSchema.from_queryset_single(
        Product.get(id=product_id)
    )


@products_router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(product_id: int) -> None:
    """
    Delete a product by its ID.

    Args:
        product_id (int): The ID of the product to delete.

    Raises:
        HTTPException: If the product is not found, a 404 error is raised.
    """
    is_exists = await Product.filter(id=product_id).exists()
    if not is_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    await Product.filter(id=product_id).delete()
