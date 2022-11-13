from fastapi import APIRouter, Response, status
from v1.mock import character

router = APIRouter()


@router.get("/", status_code=200)
async def read_character():
    return {"character": character.mock_character}
