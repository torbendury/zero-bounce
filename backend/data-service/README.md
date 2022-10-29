
# data-service

A Python 3.11 backend REST API service written to retrieve several data points from a database (tbd).

Uses [FastAPI](https://fastapi.tiangolo.com/).

## Authors

- [@torbendury](https://www.github.com/torbendury)

## Run Locally

To run the project locally, make sure you have Python 3.11 installed. If you don't, get it [here](https://www.python.org/downloads/).

When `python` is installed, install Pythons package manager `pip`:

```bash
  python -m ensurepip
```

Clone the project:

```bash
  git clone git@github.com:torbendury/zero-bounce.git
```

Go to the project directory:

```bash
  cd backend/data-service/src/
```

Create a virtual Python environment + install dependencies

```bash
  python -m virtualenv venv
  # on Windows:
  venv/scripts/activate.ps1
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
  # on Windows:
  uvicorn.exe main:app --reload
```

## Running Tests

### Unit Tests

To install testing dependencies and run tests:

```bash
  pip install -r test-requirements.txt

  python -m pytest ./
```
