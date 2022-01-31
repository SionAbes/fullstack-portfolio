FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9 as base

# Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED 1
# Force python to not write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_HOME=/etc/poetry
ENV POETRY_VERSION=1.1.5
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${POETRY_HOME}/bin:$PATH"

RUN pip install --upgrade pip && \
    wget -qO- https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV APP_MODULE='app.main:create_app'
ENV PRE_START_PATH='/usr/src/app/prestart.sh'

WORKDIR /usr/src/app


# Image for use in development
FROM base AS dev

# Install python packages with dev dependencies
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root

COPY ./alembic.ini ./
COPY ./alembic ./alembic
COPY app ./app
COPY ./tests ./tests
COPY ./prestart.sh ./prestart.sh


# Final image
FROM base 

# Install python packages
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root --no-dev

COPY ./alembic.ini ./
COPY ./alembic ./alembic
COPY app ./app
COPY ./prestart.sh ./prestart.sh
