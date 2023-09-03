# Microservices API with FastAPI, Docker and Pytest

This app is a playground to implement best practices learned from different sources.

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Remove all

```bash
docker system prune --volumes -a -f
```

```bash
docker system prune -a -f
```

## Set the default compose-file

```bash
export COMPOSE_FILE=local.yml
```

## Build / Run the Image

```bash
docker-compose -f local.yml build
```

```bash
docker-compose -f local.yml up
```

```bash
docker-compose -f local.yml up --build
```
