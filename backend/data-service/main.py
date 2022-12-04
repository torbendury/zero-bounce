import io
import yaml
from fastapi import FastAPI, status, Request
from fastapi.responses import RedirectResponse, Response
from v1.routers import archive, character
from core import database

from fastapi.middleware.cors import CORSMiddleware

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="data-service",
    version="0.0.1",
    contact={"name": "Torben Dury", "url": "https://github.com/torbendury/zero-bounce"},
)

# Only for development purposes. Needs more strict CORS settings later.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(archive.router, prefix="/archive", tags=["archive"])
app.include_router(character.router, prefix="/character", tags=["character"])


@app.get("/", status_code=status.HTTP_307_TEMPORARY_REDIRECT, response_class=RedirectResponse)
async def root(request: Request):
    return f"{str(request.url)}docs"


@app.get("/openapi.yaml", status_code=status.HTTP_200_OK)
async def openapi_yaml(request: Request):
    openapi_json = app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_json, yaml_s)
    return Response(content="---\n" + yaml_s.getvalue(), media_type="text/yaml")
