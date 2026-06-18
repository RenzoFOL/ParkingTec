from typing import Optional
from fastapi import Header, HTTPException
import jwt
import os

SECRET_KEY = os.getenv("JWT_SECRET", "RenzoIvanMichelle20232027SeguridadExtra!!")

def validate_token(
    authorization: Optional[str] = Header(None)
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Debe proporcionar el token de autorización"
        )

    try:
        token = authorization.replace("Bearer ", "")

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="El token ha expirado"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )
