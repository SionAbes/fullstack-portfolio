#!/bin/sh
cd mercedes-connected-car-adapter
pytest --cov=./src --cov-report html:./reports/coverage --cov-report xml:./reports/coverage/coverage.xml --junitxml=reports/junit/junit.xml --html=reports/junit/report.html
poetry run flake8 --exclude ./alembic --exit-zero --format=html --htmldir ./reports/flake8 --statistics --tee --output-file ./reports/flake8/flake8stats.txt
genbadge tests -o ./reports/badges/tests-badge.svg
genbadge coverage -o ./reports/badges/coverage-badge.svg
genbadge flake8 -o ./reports/badges/flake8-badge.svg