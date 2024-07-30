from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.exc import AuthExc


class Auth:
    def __init__(self, api_key: str):
        self._api_key = api_key

    security = HTTPBearer(auto_error=False)

    async def __call__(self, token: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
        if not token:
            raise AuthExc.TokenRequired

        check = self._api_key == token.credentials
        if not check:
            raise AuthExc.InvalidToken
