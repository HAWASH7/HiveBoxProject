from flask import Flask, jsonify, request, redirect, url_for
import sys
import os
import random

app = Flask(__name__)

# Load configuration from environment variables
APP_VERSION = os.getenv("APP_VERSION", "v0.0.1")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", 20.0))

# Function to print the app version and exit
def print_version():
    print(f"Current app version: {APP_VERSION}")
    sys.exit()

# Route for version
@app.route('/version', methods=['GET'])
def version():
    print_version()
    return "", 200

# Route for metrics
@app.route('/metrics', methods=['GET'])
def metrics():
    metrics_data = {
        "version": APP_VERSION,
        "default_temperature": DEFAULT_TEMPERATURE
    }
    return jsonify(metrics_data)

@app.route('/temperature', methods=['GET'])
def temperature():
    avg_temperature = random.uniform(5, 40)  
    status = "Good"

    if avg_temperature < 10:
        status = "Too Cold"
    elif avg_temperature > 37:
        status = "Too Hot"

    response = {
        "average_temperature": avg_temperature,
        "status": status
    }
    return jsonify(response)

@app.route('/')
def home():
    return "Welcome to the HiveBox API!"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify
import time

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/cache', methods=['GET'])
def get_cache():
    cache_data = redis_client.get('my_key')
    if cache_data:
        return jsonify({"data": cache_data.decode('utf-8')}), 200
    return jsonify({"error": "No data found"}), 404

@app.route('/store', methods=['POST'])
def store_data():
    redis_client.set('my_key', 'data_value', ex=300) 
    return jsonify({"message": "Data stored in cache"}), 200

from minio import Minio

minio_client = Minio('localhost:9000',
                      access_key='minioadmin',
                      secret_key='minioadmin',
                      secure=False)

@app.route('/store', methods=['POST'])
def store_data():
    redis_client.set('my_key', 'data_value', ex=300)

    minio_client.put_object('mybucket', 'data_object', data=b'data_value', length=len(b'data_value'))
    return jsonify({"message": "Data stored in Redis and MinIO"}), 200


@app.route('/metrics', methods=['GET'])
def metrics():
    return jsonify({"message": "Metrics extended"}), 200



@app.route('/readyz', methods=['GET'])
def readyz():
    return "", 200 

