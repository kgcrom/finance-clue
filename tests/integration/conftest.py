"""Pytest configuration for integration tests."""

from os import environ

import pytest

from stock_clue.opendart import OpenDartClient
from stock_clue.openkis import OpenKisClient


@pytest.fixture(scope="session")
def integration_opendart_client() -> OpenDartClient:
    """Instantiates a opendart Client for use with integration tests."""

    token = environ.get("OPENDART_API_KEY", None)
    return OpenDartClient(token=token)


@pytest.fixture(scope="session")
def integration_openkis_client() -> OpenKisClient:
    """Instantiates a openkis Client for use with integration tests."""

    app_key = environ.get("OPENKIS_APP_KEY", None)
    app_secret = environ.get("OPENKIS_APP_SECRET", None)

    return OpenKisClient(app_key, app_secret, True)
