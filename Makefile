# SPDX-FileCopyrightText: 2024 Helmholtz-Zentrum hereon GmbH
#
# SPDX-License-Identifier: CC0-1.0

.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8 lint/black
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

NPROCS ?= 1

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test clean-venv clean-c ## remove all build, virtual environments, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-venv:  # remove the virtual environment
	rm -rf venv

clean-c:  # remove the cython-derived c-code
	rm -rf psy_ugrid/*.c
	rm -rf psy_ugrid/*.so

lint/isort: ## check style with flake8
	isort --check psy_ugrid tests
lint/flake8: ## check style with flake8
	flake8 psy_ugrid tests
lint/black: ## check style with black
	black --check psy_ugrid tests
	blackdoc --check psy_ugrid tests
lint/reuse:  ## check licenses
	reuse lint

lint: lint/isort lint/black lint/flake8  lint/reuse ## check style

formatting:
	isort psy_ugrid tests
	black psy_ugrid tests
	blackdoc psy_ugrid tests

quick-test: ## run tests quickly with the default Python
	python -m pytest

pipenv-test: ## run tox
	pipenv run tox --current-env

test: ## run tox
	tox

test-all: test test-docs ## run tests and test the docs

coverage: ## check code coverage quickly with the default Python
	python -m pytest --cov psy_ugrid --cov-report=html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

test-docs: ## generate Sphinx HTML documentation, including API docs
	$(MAKE) -C docs clean
	$(MAKE) -C docs linkcheck

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build --sdist
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python -m pip install .

dev-install:
	python -m pip install -r docs/requirements.txt
	python -m pip install -e .[dev]
	pre-commit install

venv-install: clean-venv
	python -m venv venv
	venv/bin/python -m pip install -r docs/requirements.txt
	venv/bin/python -m pip install -e .[dev]
	venv/bin/pre-commit install
