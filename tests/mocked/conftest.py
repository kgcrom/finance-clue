import pytest

from stock_clue.opendart import OpenDartClient
from stock_clue.openkis import OpenKisClient


@pytest.fixture(scope="module")
def mock_opendart_client_url() -> str:
    """Returns a url for the mocked OpenDartClient client"""
    return "https://mocked.local/api"


@pytest.fixture(scope="module")
def mock_opendart_client(mock_opendart_client_url: str) -> OpenDartClient:
    """Returns a mocked OpenDartClient client"""
    return OpenDartClient("", endpoint=mock_opendart_client_url)


@pytest.fixture(scope="module")
def mock_openkis_client_url() -> str:
    """Returns a url for the mocked OpenKisClient client"""
    return "https://mocked.local"


@pytest.fixture(scope="module")
def mock_openkis_client(mock_openkis_client_url: str) -> OpenKisClient:
    """Returns a mocked OpenKisClient client"""
    return OpenKisClient("", "", endpoint=mock_openkis_client_url)
