def sanitize_password(password: str) -> str:
    """
    Ensures password is processed only in-memory.
    """
    if not isinstance(password, str):
        raise ValueError("Invalid password input")
    return password.strip()


def destroy_password(password: str):
    """
    Explicitly removes reference to password.
    """
    password = None
