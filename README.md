[![Flake8 Status](./fastapi-master-api/reports/flake8/flake8-badge.svg?dummy=8484744)](./fastapi-master-api/reports/flake8/index.html)
[![Tests Status](./reports/junit/junit-badge.svg?dummy=8484744)](./reports/junit/report.html)
# Siôn Abraham Full-Stack Portfolio
Last updated: 25/12/2021

This is a overview of my full-stack toolset which will constantly evolve as I grow as a developer. My current aims are to showcase the technologies I either enjoy personally using, or ones that I have had much exposure to. The goals of this repo is to:
 - Robust backend API with authenication, authorization, and a full set of CRUD endpoints.
 - Multiple autogeneration techniques, especially for API documentation.
 - A modern single page application frontend
 - CI pipeline, with automated unit/integration tests
 - Suite of E2E tests
 - Orchestration scripts for Kubernetes

## Tech

As currently implemented:

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management using python type annotations.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - A lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [Docker](https://www.docker.com/) - Package applications as portable container images to run in any environment consistently.
- [openapi-generate](https://github.com/OpenAPITools/openapi-generator) - Allows generation of API client libraries.

## How to Run
Create a `.env` file using the `.env.example` file then run the follwing `makefile` command:

```
make clean && make run-backend
```

## License

MIT

**Free Software, Hell Yeah!**
