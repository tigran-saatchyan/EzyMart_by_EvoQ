from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends

from ezymart_by_evoq.auth.schemas import oauth2_scheme
from ezymart_by_evoq.users import schemas
from ezymart_by_evoq.users.models import User
from ezymart_by_evoq.users.services import get_current_user
from ezymart_by_evoq.users.utils import hash_password

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post(
    "/register/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.User_Pydantic
)
async def register(
    user_data: schemas.UserInPydantic
):
    user_data.validate_password()

    user_data = user_data.model_dump(
        exclude_unset=True,
        exclude={"password2"}
    )

    user_data["password"] = hash_password(user_data.get("password"))
    user = await User.create(
        **user_data
    )

    return await schemas.User_Pydantic.from_tortoise_orm(user)


@user_router.get("/")
def get_user(
    user: Annotated[schemas.User_Pydantic, Depends(get_current_user)]
):
    return user

# @user_router.get("/", response_model=List[User_Pydantic])
# async def get_users():
#     return await User_Pydantic.from_queryset(User.all())


# @user_router.post("/", response_model=User_Pydantic)
# async def create_user(user: UserIn_Pydantic):
#     user_obj = await User.create(**user.model_dump(exclude_unset=True))
#     return await User_Pydantic.from_tortoise_orm(user_obj)

#
# @user_router.get("/{user_id}", response_model=User_Pydantic)
# async def get_user(user_id: int):
#     return await User_Pydantic.from_queryset_single(User.get(id=user_id))
#
#
# @user_router.put("/{user_id}", response_model=User_Pydantic)
# async def update_user(user_id: int, user: UserIn_Pydantic):
#     await User.filter(id=user_id).update(**user.model_dump(
#     exclude_unset=True))
#     return await User_Pydantic.from_queryset_single(User.get(id=user_id))
#
#
# @user_router.delete("/{user_id}", response_model=Status)
# async def delete_user(user_id: int):
#     deleted_count = await User.filter(id=user_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not
#         found")
#     return Status(message=f"Deleted user {user_id}")
