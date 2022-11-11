# docker-compose

This directory contains a `docker-compose-yml` to run the included services locally.

## Starting, Stopping, Cleaning

To start everything up, run

```bash
    docker-compose up
    # in newer versions, docker-compose is baked into docker itself
    docker compose up
    # to run in "detached" mode (so you can use your terminal for other stuff)
    docker compose up -d
```

To stop everything, just hit `Ctrl+C` when the composition is attached to your terminal. Otherwise, run

```bash
    docker-compose down
    # in newer versions, docker-compose is baked into docker itself
    docker compose down
```

To clean everything up (most interesting for the database, but also for the Docker images on your machine), run

```bash
    docker compose down
    docker volume prune -f
```

This will terminate any services still running from your `docker-compose` and will delete the `postgres` volume holding the data.

## Included services

### backend data-service

`data-service` freshly baked into a Docker container when starting everything up. Will connect to the PostgreSQL database instance when starting up.
Waits until `postgres` and (as soon as implemented) `mongodb` become ready.

### frontend

To be done.

### postgres

Initially, an empty PostgreSQL single node instance. A `postgres` docker volume will be created that holds the data created and/or modified within your local running instance of zero-bounce.

#### `_sql` directory

This directory holds SQL files to fill the database initially with a) the tables and b) some example data. They shouldn't be needed for case a) anymore as soon as the `data-service` also starts up with the PostgreSQL database, because `psycopg2` together with `sqlalchemy` will ensure that the tables are present and according to the DB model defined in the service itself.

### mongodb

To be done.
