from fastapi import APIRouter, Response, status
from v1.mock import character

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def read_character():
    return {"character": character.mock_character}
