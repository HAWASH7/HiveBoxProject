from flask import Flask, render_template, request, redirect, url_for
import sys
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

APP_VERSION = "v0.0.1"

def print_version():
    print(f"Current app version: {APP_VERSION}")
    sys.exit()

@app.route('/version', methods=['GET'])
def version():
    print_version()
    return "", 200  
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-sensor-data', methods=['GET', 'POST'])
def add_sensor_data():
    if request.method == 'POST':
        sensor_data = request.form['sensor_data']
        print(f"Received sensor data: {sensor_data}")
        return redirect(url_for('home'))
    return render_template('add_sensor_data.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    response = requests.get('https://api.opensensemap.org/boxes')
    return response.json(), response.status_code



@app.route('/temperature', methods=['GET'])
def get_average_temperature():
    try:
        response = requests.get('https://api.opensensemap.org/boxes', timeout=5)
        response.raise_for_status()

        boxes = response.json()
        total_temp = 0
        count = 0

        # Check each box for temperature data
        for box in boxes:
            # Assuming each box has a 'sensorData' key with temperature data
            for sensor in box.get('sensorData', []):
                if sensor['type'] == 'temperature':
                    # Check if data is within the last hour
                    timestamp = datetime.fromisoformat(sensor['timestamp'])
                    if datetime.now() - timestamp <= timedelta(hours=1):
                        total_temp += sensor['value']
                        count += 1

        if count == 0:
            return {"error": "No recent temperature data available"}, 404  # Not found if no data

        average_temp = total_temp / count
        return {"average_temperature": average_temp}, 200

    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}, 408
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500
