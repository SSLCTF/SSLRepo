import os

from fastapi import APIRouter

from core.api.v1.dto.flag import FlagReponse
from starlette import status

router = APIRouter(prefix="/flag", tags=["API/v1/Flag"])


@router.get(
    "",
    response_model=FlagReponse,
    status_code=status.HTTP_200_OK,
    summary="Возвращяет флаг"
)
async def get_flag():
    flag = os.getenv("CTF_FLAG")

    return FlagReponse(flag=flag)

