from flask import Flask, render_template, request, redirect, url_for
import sys
import requests

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
