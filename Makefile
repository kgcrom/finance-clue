LOCAL_KRX_SPEC_FILE=OpenKrx-public.yml
LOCAL_KIS_SPEC_FILE=OpenKis-public.yml
LOCAL_DART_SPEC_FILE=OpenDart-public.yml

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

.PHONY: install
install:
ifneq (, $(shell which poetry))
	poetry install
else
	@(echo "poetry is not installed. See https://python-poetry.org/docs/#installation for more info."; exit 1)
endif

.PHLY: dev-dependencies
dev-dependencies:
	npm install -D

.PHONY: download-kis-spec
download-kis-spec:
	@echo Downloading KIS spec; \
	touch OpenKis-public.yml && \
	curl https://raw.githubusercontent.com/kgcrom/finance-openapi/main/docs/OpenKis-public.yml -o $(LOCAL_KIS_SPEC_FILE)

.PHONY: generate-openkis
ifndef KIS_SPEC_FILE
generate-openkis: KIS_SPEC_FILE = $(LOCAL_KIS_SPEC_FILE)
generate-openkis: install 
endif
generate-openkis: dev-dependencies download-kis-spec
	npm run autorest -- openkis_client_gen_config.md \
		--use:@autorest/modelerfour@4.27.0 \
		--use:@autorest/python@6.13.15 \
		--input-file=$(KIS_SPEC_FILE)
	@poetry run black .
	@poetry run isort .

.PHONY: download-krx-spec
download-krx-spec:
	@echo Downloading KRX spec; \
	touch OpenKrx-public.yml && \
	curl https://raw.githubusercontent.com/kgcrom/finance-openapi/main/docs/OpenKrx-public.yml -o $(LOCAL_KRX_SPEC_FILE)

.PHONY: generate-openkrx
ifndef KRX_SPEC_FILE
generate-openkrx: KRX_SPEC_FILE = $(LOCAL_KRX_SPEC_FILE)
generate-openkrx: install 
endif
generate-openkrx: dev-dependencies download-krx-spec
	npm run autorest -- openkrx_client_gen_config.md \
		--use:@autorest/modelerfour@4.27.0 \
		--use:@autorest/python@6.13.15 \
		--input-file=$(KRX_SPEC_FILE)
	@poetry run black .
	@poetry run isort .

.PHONY: download-dart-spec
download-dart-spec:
	@echo Downloading DART spec; \
	touch OpenDart-public.yml && \
	curl https://raw.githubusercontent.com/kgcrom/finance-openapi/main/docs/OpenDart-public.yml -o $(LOCAL_DART_SPEC_FILE)

.PHONY: generate-opendart
ifndef DART_SPEC_FILE
generate-opendart: DART_SPEC_FILE = $(LOCAL_DART_SPEC_FILE)
generate-opendart: install
endif
generate-opendart: dev-dependencies download-dart-spec
	npm run autorest -- opendart_client_gen_config.md \
		--use:@autorest/modelerfour@4.27.0 \
		--use:@autorest/python@6.13.15 \
		--input-file=$(DART_SPEC_FILE)
	@poetry run black .
	@poetry run isort .

