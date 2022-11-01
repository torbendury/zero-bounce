import uuid
from fastapi import FastAPI, Response, status
from routers import archive, character

app = FastAPI()

app.include_router(archive.router, prefix="/archive", tags=["archive"])
app.include_router(character.router, prefix="/character", tags=["character"])


@app.get("/", status_code=status.HTTP_404_NOT_FOUND)
async def root(response: Response):
    return {"error": "Not found"}
