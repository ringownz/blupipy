# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Development Requirements

- Python3.11.0
- Pip
- Poetry (Python Package Manager)


## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make up`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
