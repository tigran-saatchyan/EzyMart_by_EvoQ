import re

from fastapi import HTTPException
from starlette import status
from tortoise.validators import Validator


class EmailValidator(Validator):
    """
    Validate an email address for basic format compliance.

    This function checks if the given email address follows a basic format:
    - It contains only valid characters including letters, numbers, and
        certain special characters.
    - It has the "@" symbol followed by a domain name.

    Args:
        email_address (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """

    def __call__(self, email_address: str):
        if not re.search(
                r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                email_address
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"The email address {email_address} is not valid"

            )


class PasswordValidator(Validator):

    def __call__(self, password: str):
        if not re.search(
                r"^(?=.*[A-Z])(?=.*[$%&!]).{8,}$",
                password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The password is not valid"

            )
