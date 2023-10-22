black:
	poetry run black .

isort:
	poetry run isort .

mypy:
	poetry run mypy .

pylint:
	poetry run pylint $(shell git ls-files '*.py')

checklist: black isort mypy pylint

export_requirement:
	poetry export -f requirements.txt --output requirements.txt
