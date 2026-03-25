import os

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt


http_bearer = HTTPBearer()

SECRET = os.getenv("JWT_KEY")
ALGORITHM = os.getenv("JWT_ALG")

def ctf_policy(
    credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")

    return payload