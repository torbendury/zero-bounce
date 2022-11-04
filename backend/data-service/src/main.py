import uuid
from fastapi import FastAPI, Response, status
from routers import archive, character
from mock import archive as archiveMock
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(archive.router, prefix="/archive", tags=["archive"])
app.include_router(character.router, prefix="/character", tags=["character"])


@app.get("/", status_code=status.HTTP_404_NOT_FOUND)
async def root(response: Response):
    return {"error": "Not found"}
