from fastapi.testclient import TestClient

# local imports
from server import main

client = TestClient(main.app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['health_check'] == 'ok'