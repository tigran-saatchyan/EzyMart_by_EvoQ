from typing import Optional

import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from ezymart_by_evoq.core import config
from ezymart_by_evoq.product.routes.routes import products_router

app = FastAPI()

register_tortoise(
    app,
    db_url=config.DATABASE_URL,
    modules={"models": [*config.MODELS]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(products_router)

if __name__ == '__main__':
    uvicorn.run(
        "ezymart_by_evoq.main:app", host="localhost", port=8000, reload=True
    )
