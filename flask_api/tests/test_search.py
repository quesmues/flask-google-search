import time

import pytest

from flask_api.app import app
from flask_api.main.routes import get_search_data


@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as testing_client:
        yield testing_client


def test_get_scrap_google_search(test_client):
    """
    Teste da rota "/api/v1/scrap-google-search"
    """
    response = test_client.get('/api/v1/scrap-google-search?search=teste')
    assert response.status_code == 200
    assert b"links" in response.data and b"search_text" in response.data


def test_get_search_data():
    """
    Teste unitário da função "get_search_data"
    """
    data = get_search_data("teste")
    assert isinstance(data, dict)
    assert data.get("search_text", None)
    assert data.get("links", None)
