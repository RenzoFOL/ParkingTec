import os
from fastapi import Header, HTTPException
import jwt

SECRET_KEY = os.getenv("JWT_SECRET", "RenzoIvanMichelle20232027SeguridadExtra!!")

def validate_token(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token invalido"
        )
