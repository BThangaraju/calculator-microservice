import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=3&b=2')
    assert response.get_json() == {"result": 5}

def test_subtract(client):
    response = client.get('/subtract?a=5&b=2')
    assert response.get_json() == {"result": 3}
