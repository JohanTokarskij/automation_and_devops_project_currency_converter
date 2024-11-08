import pytest
import requests

from app import app, API_URL, API_KEY

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Verify that the home page loads successfully and contains 'Currency Converter'."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Currency Converter' in response.data


def test_api_connection():
    """Ensure the API connection is successful and returns a valid USD conversion rate."""
    params = {
        'apikey': API_KEY,
        'base_currency': 'EUR',
        'currencies': 'USD'
    }
    response = requests.get(API_URL, params=params)
    assert response.status_code == 200

    data = response.json()
    assert 'data' in data
    assert 'USD' in data['data']
    assert isinstance(data['data']['USD'], float)
