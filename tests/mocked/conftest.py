import pytest

from stock_clue.opendart import OpenDartClient


@pytest.fixture(scope="module")
def mock_client_url():
    """Returns a url for the mocked OpenDartClient client"""
    return "https://mocked.local/api"


@pytest.fixture(scope="module")
def mock_client(mock_client_url) -> OpenDartClient:
    """Returns a mocked OpenDartClient client"""
    return OpenDartClient("", endpoint=mock_client_url)
