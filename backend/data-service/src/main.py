import uuid
from fastapi import FastAPI, Response, status
from routers import archive

app = FastAPI()

app.include_router(archive.router)


@app.get("/", status_code=status.HTTP_404_NOT_FOUND)
async def root(response: Response):
    return {"error": "Not found"}
