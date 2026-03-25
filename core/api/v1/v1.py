from fastapi import APIRouter, Depends

from core.api.v1 import flag
from dependency.auth import ctf_policy


router = APIRouter(prefix="/v1")

router.include_router(flag.router, dependencies=[Depends(ctf_policy)])