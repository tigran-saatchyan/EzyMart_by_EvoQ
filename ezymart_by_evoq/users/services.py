from typing import Annotated

from fastapi import Depends

from ezymart_by_evoq.auth.schemas import oauth2_scheme
from ezymart_by_evoq.auth.services import get_email_from_token
from ezymart_by_evoq.users import schemas
from ezymart_by_evoq.users.models import User


async def get_current_user(
    access_token: Annotated[str, Depends(oauth2_scheme)]
):
    email = get_email_from_token(access_token)
    user = await User.filter(email=email).first()
    return await schemas.User_Pydantic.from_tortoise_orm(user)
