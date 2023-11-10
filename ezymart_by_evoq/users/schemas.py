from fastapi import HTTPException, status
from pydantic import BaseModel, Field, field_validator, EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from ezymart_by_evoq.users.models import User
from ezymart_by_evoq.users.validatiors import PasswordValidator

User_Pydantic = pydantic_model_creator(
    User,
    name="User",
    exclude=("password",)
)


class UserInPydantic(BaseModel):
    email: EmailStr = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    password2: str = Field(..., max_length=255)
    first_name: str | None = Field(None, max_length=255)
    last_name: str | None = Field(None, max_length=255)
    telephone: str | None = Field(None, max_length=255)
    telegram_user_id: int | None = Field(None)
    country: str | None = Field(None, max_length=255)
    city: str | None = Field(None, max_length=255)

    def validate_password(self):
        if self.password != self.password2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match"
            )
        validator = PasswordValidator()
        validator(self.password)

