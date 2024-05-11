.PHONY: lint
lint:
	poetry run black .
	poetry run isort .
	poetry run mypy .
	poetry run pylint $(shell git ls-files '*.py')
