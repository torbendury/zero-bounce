# Lightweight debian based Python 3.11 base image
FROM python:3.11.0-slim-bullseye as base

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Do those above steps first, as they will not change often. This will dramatically improve build time.
# Below, we're copying our code (which changes on every build) into the container as well as running package updates.

RUN apt update && apt upgrade -y

COPY ./src/ /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]