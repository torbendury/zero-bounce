from fastapi import APIRouter, Response, status
from mock import archive


router = APIRouter()


@router.get("/archive/categories", status_code=200)
async def read_categories():
    return {"categories": archive.mock_categories}


@router.get("/archive/categories/{category_id}", status_code=200)
async def read_category(category_id: int, response: Response):
    for c in archive.mock_categories:
        if category_id == c["id"]:
            return c
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "The specified category id does not exist"}


@router.get("/archive/categories/{category_id}/entries/{entry_id}", status_code=200)
async def read_category_entry(category_id: int, entry_id: int, response: Response):
    for c in archive.mock_categories:
        if category_id == c["id"]:
            for e in c["data"]:
                if entry_id == e["id"]:
                    return e
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "The specified category or entry id does not exist"}
