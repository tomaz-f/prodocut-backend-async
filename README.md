# Product-Backend

This project is an example of a dockerized fastapi application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Installation

Use poetry to manage this project

To start the virtual environment.

```bash
poetry shell
```

To install the project dependencies.

```bash
poetry install
```

## ENV EXAMPLES

| ENVs                     | ENV_EXAMPLE                                                     |
| ------------------------ | --------------------------------------------------------------- |
| POSTGRES_USER            | admin                                                           |
| POSTGRES_PASSWORD        | admin                                                           |
| POSTGRES_DB              | main                                                            |
| PGADMIN_DEFAULT_EMAIL    | admin@gmail.com                                                 |
| PGADMIN_DEFAULT_PASSWORD | admin                                                           |
| DB_URL                   | postgresql+psycopg2://postgresql/main?user=admin&password=admin |

## How to run this project

Build the app into a docker image:

```bash
docker build . -t <project_name>
```

Using docker compose to run the containers.

```bash
docker compose up -d
```

Initiate the alembic migrations

```bash
docker compose run --user 1000 app sh -c 'alembic init migrations'
```

Set the alembic env in migrations folders:
copy the code inside alembic_env_example.py to /migrations/env.py

Generate the migrations

```bash
docker compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add categories table"'
```

Upgrade the database:

```bash
docker compose run --user 1000 app sh -c 'alembic upgrade head'
```
