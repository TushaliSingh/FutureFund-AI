import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a plain-text password.
    """

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a password against its hash.
    """

    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )
