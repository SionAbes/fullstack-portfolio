#!/bin/sh
cd fastapi-master-api
pytest --junitxml=reports/junit/junit.xml --html=reports/junit/report.html
poetry run coverage xml -o ./reports/coverage/coverage.xml --omit="*/test*"
poetry run coverage html -d ./reports/coverage --omit="*/test*"
poetry run flake8 --exclude ./alembic --exit-zero --format=html --htmldir ./reports/flake8 --statistics --tee --output-file ./reports/flake8/flake8stats.txt
genbadge tests -o ./reports/badges/tests-badge.svg
genbadge coverage -o ./reports/badges/coverage-badge.svg
genbadge flake8 -o ./reports/badges/flake8-badge.svg