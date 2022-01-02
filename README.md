### Project
[![Last Commit](https://img.shields.io/github/last-commit/SionAbes/fullstack-portfolio)](https://github.com/SionAbes/fullstack-portfolio/commits/master)
[![HitCount](http://hits.dwyl.com/SionAbes/fullstack-portfolio.svg?style=flat-square)](http://hits.dwyl.com/SionAbes/fullstack-portfolio)
[![License Status](https://img.shields.io/github/license/SionAbes/fullstack-portfolio)](https://github.com/SionAbes/fullstack-portfolio/blob/master/LICENSE.md)
### FastAPI Master API
[![Flake8 Status](./fastapi-master-api/reports/badges/flake8-badge.svg?dummy=8484744)](https://sionabes.github.io/fullstack-portfolio/fastapi-master-api/reports/flake8/index.html)
[![Tests Status](./fastapi-master-api/reports/badges/tests-badge.svg?dummy=8484744)](https://sionabes.github.io/fullstack-portfolio/fastapi-master-api/reports/junit/report.html)
[![Coverage Status](./fastapi-master-api/reports/badges/coverage-badge.svg?dummy=8484744)](https://sionabes.github.io/fullstack-portfolio/fastapi-master-api/reports/coverage/index.html)
![FastAPI CI](https://github.com/SionAbes/fullstack-portfolio/actions/workflows/fastapi-master-api-ci.yaml/badge.svg)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Python 3.9](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue)

### Mercedes Connected Car Adapter
[![Flake8 Status](./mercedes-connected-car-adapter/reports/badges/flake8-badge.svg?dummy=8484744)](https://sionabes.github.io/fullstack-portfolio/mercedes-connected-car-adapter/reports/flake8/index.html)
[![Tests Status](./mercedes-connected-car-adapter/reports/badges/tests-badge.svg?dummy=8484744)](https://sionabes.github.io/fullstack-portfolio/mercedes-connected-car-adapter/reports/junit/report.html)
[![Coverage Status](./mercedes-connected-car-adapter/reports/badges/coverage-badge.svg?dummy=8484744)](https://sionabes.github.io/fullstack-portfolio/mercedes-connected-car-adapter/reports/coverage/index.html)
![Mercedes Connected Car Adapter CI](https://github.com/SionAbes/fullstack-portfolio/actions/workflows/mercedes-connected-car-ci.yaml/badge.svg)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Python 3.9](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue)

# Siôn Abraham Full-Stack Portfolio
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
- [GitHub Actions](https://github.com/features/actions) -  Automate all your software workflows with build, test, and deploy from GitHub.

## How to Run
Create a `.env` file using the `.env.example` file then run the follwing `makefile` command:

```
make clean && make run-backend
```

## License

MIT

**Free Software, Hell Yeah!**
