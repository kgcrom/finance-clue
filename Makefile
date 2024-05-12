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

.PHONY: generate-openkis
generate-openkis:
	npm run autorest -- openkis_client_gen_config.md \
		--use:@autorest/modelerfour@4.27.0 \
		--use:@autorest/python@6.13.15

.PHONY: generate-opendart
generate-opendart:
	npm run autorest -- opendart_client_gen_config.md \
		--use:@autorest/modelerfour@4.27.0 \
		--use:@autorest/python@6.13.15
