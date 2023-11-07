from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from tortoise.contrib.fastapi import register_tortoise

from ezymart_by_evoq.core import config
from ezymart_by_evoq.product.routes import products_router


def create_app():
    application = FastAPI()
    return application


def setup_database(application: FastAPI) -> None:
    register_tortoise(
        application,
        db_url=config.DATABASE_URL,
        modules={"models": [*config.MODELS]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


def setup_cors(application: FastAPI) -> None:
    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def setup_routes(application: FastAPI) -> None:
    application.include_router(products_router)


def custom_openapi(application: FastAPI) -> Dict[str, dict]:
    if application.openapi_schema:
        return application.openapi_schema
    openapi_schema = get_openapi(
        title="EzyMart by EvoQ API",
        version="1.0.0",
        summary="E-Commerce API solution for developers",
        description="**EzyMart by EvoQ API** is a tool that allows "
                    "developers to integrate e-commerce features "
                    "like product management, inventory control, "
                    "order processing, and customer data management "
                    "into their applications or websites, making it "
                    "easier to run online stores.",
        routes=application.routes,
        terms_of_service="",
        contact={
            "name": "Tigran Saatchyan (EvoQ) - Backend Developer",
            "url": "https://github.com/tigran-saatchyan",
        },
        license_info={
            "name": "MIT License",
            "url": "https://opensource.org/licenses/MIT",
        },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    application.openapi_schema = openapi_schema
    return application.openapi_schema
