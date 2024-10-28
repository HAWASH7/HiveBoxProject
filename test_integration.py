import os
import pytest
from flask import Flask
from your_flask_app import app  # replace 'your_flask_app' with your actual app filename

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_version(client):
    response = client.get('/version')
    assert response.status_code == 200

def test_metrics(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"version" in response.data

def test_temperature(client):
    response = client.get('/temperature')
    assert response.status_code == 200
    data = response.get_json()
    assert "average_temperature" in data
    assert "status" in data

import requests

def test_version_endpoint():
    response = requests.get("http://hivebox.local/version")
    assert response.status_code == 200

def test_temperature_endpoint():
    response = requests.get("http://hivebox.local/temperature")
    assert response.status_code == 200
