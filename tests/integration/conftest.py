"""Pytest configuration for integration tests."""

from os import environ

import pytest

from finance_clue.opendart import OpenDartClient
from finance_clue.openkis import OpenKisClient
from finance_clue.openkrx import OpenKrxClient


@pytest.fixture(scope="session")
def integration_opendart_client() -> OpenDartClient:
    """Instantiates an opendart Client for use with integration tests."""

    token = environ.get("OPENDART_API_KEY", None)
    return OpenDartClient(token=token)


@pytest.fixture(scope="session")
def integration_openkis_client() -> OpenKisClient:
    """Instantiates an openkis Client for use with integration tests."""

    app_key = environ.get("OPENKIS_APP_KEY", None)
    app_secret = environ.get("OPENKIS_APP_SECRET", None)
    client = OpenKisClient(app_key, app_secret)
    client.init()
    return client


@pytest.fixture(scope="session")
def integration_openkrx_client() -> OpenKrxClient:
    """Instantiates an openkrx Client for use with integration tests."""

    auth_key = environ.get("OPENKRX_AUTH_KEY", None)

    return OpenKrxClient(auth_key)
