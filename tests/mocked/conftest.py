import pytest

from finance_clue.opendart import OpenDartClient
from finance_clue.openkis import OpenKisClient
from finance_clue.openkrx._patch import OpenKrxClient


@pytest.fixture(scope="module")
def mock_opendart_client_url() -> str:
    """Returns a url for the mocked OpenDartClient"""
    return "https://mocked.local/api"


@pytest.fixture(scope="module")
def mock_opendart_client(mock_opendart_client_url: str) -> OpenDartClient:
    """Returns a mocked OpenDartClient"""
    return OpenDartClient("", endpoint=mock_opendart_client_url)


@pytest.fixture(scope="module")
def mock_openkis_client_url() -> str:
    """Returns a url for the mocked OpenKisClient"""
    return "https://mocked.local"


@pytest.fixture(scope="module")
def mock_openkis_client(mock_openkis_client_url: str) -> OpenKisClient:
    """Returns a mocked OpenKisClient"""
    return OpenKisClient("key", "secret", endpoint=mock_openkis_client_url)


@pytest.fixture(scope="module")
def mock_openkrx_client_url() -> str:
    """Returns a url for the mocked OpenKrxClient"""
    return "https://mocked.local"


@pytest.fixture(scope="module")
def mock_openkrx_client(mock_openkrx_client_url: str) -> OpenKrxClient:
    """Returns a mocked OpenKrxClient"""
    return OpenKrxClient("", endpoint=mock_openkrx_client_url)
