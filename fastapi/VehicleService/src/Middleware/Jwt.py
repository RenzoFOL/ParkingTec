from fastapi import Header, HTTPException
import jwt

SECRET_KEY = "mi_clave"

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
            detail="Token inválido"
        )