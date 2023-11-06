from fastapi import HTTPException
from starlette import status

from ezymart_by_evoq.product.models import Product


async def is_product_exists(product_id: int) -> None:
    is_exists = await Product.filter(id=product_id).exists()
    if not is_exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
