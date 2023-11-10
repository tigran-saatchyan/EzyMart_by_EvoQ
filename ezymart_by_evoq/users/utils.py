import hashlib
import hmac

from ezymart_by_evoq.service.constants import (
    PWD_HASH_ITERATIONS,
    PWD_HASH_SALT,
    CRYPTOGRAPHIC_HASH_FUNCTION,
)


def hash_password(password):
    """
    Hash a password using a cryptographic hash function.

    :param password: The password to hash.

    :return: The hashed password.
    """
    return hashlib.pbkdf2_hmac(
        CRYPTOGRAPHIC_HASH_FUNCTION,
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )


async def compare_passwords(db_pwd, received_pwd) -> bool:
    """
    Compares two passwords for equality.

    :param db_pwd: A base64 encoded hashed password string from
        the database.
    :param received_pwd: A plain text password string received from
        the user.

    :return: A boolean indicating whether the passwords match.
    """
    db_password = db_pwd
    received_password = str(hashlib.pbkdf2_hmac(
        CRYPTOGRAPHIC_HASH_FUNCTION,
        received_pwd.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ))
    is_equal = hmac.compare_digest(
        db_password,
        received_password
    )
    return is_equal
