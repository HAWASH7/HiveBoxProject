from app import app

def test_version():
    client = app.test_client()
    response = client.get('/version')
    assert response.status_code == 200

def test_get_sensor_data():
    client = app.test_client()
    response = client.get('/sensor-data')
    assert response.status_code == 200

def test_get_average_temperature():
    client = app.test_client()
    response = client.get('/temperature')
    assert response.status_code in (200, 404)  # It should either return 200 or 404
