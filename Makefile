.PHONY: black
black:
	poetry run black .

.PHONY: isort
isort:
	poetry run isort .

.PHONY: mypy
mypy:
	poetry run mypy .

.PHONY: pylint
pylint:
	poetry run pylint $(shell git ls-files '*.py')

.PHONY: lint
lint: black isort mypy pylint
