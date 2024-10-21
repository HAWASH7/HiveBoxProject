from flask import Flask, render_template, request, redirect, url_for
import sys

app = Flask(__name__)

# Define the app version
APP_VERSION = "v0.0.1"

# Function to print the app version and exit
def print_version():
    print(f"Current app version: {APP_VERSION}")
    sys.exit()

# Route for version
@app.route('/version', methods=['GET'])
def version():
    print_version()
    return "", 200  # Just to return a response status

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the form
@app.route('/add-sensor-data', methods=['GET', 'POST'])
def add_sensor_data():
    if request.method == 'POST':
        sensor_data = request.form['sensor_data']
        print(f"Received sensor data: {sensor_data}")
        return redirect(url_for('home'))
    return render_template('add_sensor_data.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
