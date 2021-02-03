
from main import app
from flask import json

def test_main_get_html():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'

def test_main_get_json():
    response = app.test_client().get('/', headers={'Accept': 'application/json'})

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['message'] == 'Hello, World'

def test_main_post_html():
    response = app.test_client().post('/')

    assert response.status_code == 200
    assert response.data == b'<p>Hello, World</p>'

def test_main_post_json():
    response = app.test_client().post('/', headers={'Accept': 'application/json'})

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['message'] == 'Hello, World'
