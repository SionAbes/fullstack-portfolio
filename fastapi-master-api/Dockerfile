FROM python:3.10 as base

# Force the stdout and stderr streams to be unbuffered
ENV PYTHONUNBUFFERED 1
# Force python to not write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_HOME=/etc/poetry
ENV POETRY_VERSION=1.1.11
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${POETRY_HOME}/bin:$PATH"

RUN pip install --upgrade pip && \
    curl -sSL https://install.python-poetry.org | python3 -


WORKDIR /usr/src/app


# Image for use in development
FROM base AS dev

# Install python packages with dev dependencies
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root

COPY app ./app
COPY ./tests ./tests


# Final image
FROM base 

# Install python packages
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --no-root --no-dev

COPY app ./app


CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "80"]
