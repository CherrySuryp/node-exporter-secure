from fastapi import HTTPException, status


class AuthExc:
    TokenRequired = HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    InvalidToken = HTTPException(status_code=status.HTTP_404_NOT_FOUND)
