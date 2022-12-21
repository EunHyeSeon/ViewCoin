import pytest
import json
import app

@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_app(client):
    rv = client.get('/', data=dict(
      ), follow_redirects=True)
    assert 'ok' in json.loads(rv.data.decode("utf-8"))['status']

    rv = client.post('/select', data=dict(
      name='Litecoin'
    ), follow_redirects=True)
    assert 'error' in json.loads(rv.data.decode("utf-8"))['status']

    rv = client.post('/minmax', data=dict(
      name='Litecoin'
    ), follow_redirects=True)
    assert 'error' in json.loads(rv.data.decode("utf-8"))['status']

    rv = client.get('/intro', data=dict(
    ), follow_redirects=True)
    assert 'error' in json.loads(rv.data.decode("utf-8"))['status']