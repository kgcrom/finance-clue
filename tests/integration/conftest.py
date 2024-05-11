"""Pytest configuration for integration tests."""

from os import environ

import pytest

from stock_clue.opendart import OpenDartClient


@pytest.fixture(scope="session")
def integration_client() -> OpenDartClient:
    """Instantiates a opendart Client for use with integration tests."""

    token = environ.get("OPENDART_API_KEY", None)
    return OpenDartClient(token=token)
