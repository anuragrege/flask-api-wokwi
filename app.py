from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

@app.route('/sensor_data', methods=['POST'])
def receive_data():
    start_time = time.time()
    data = request.get_json()
    print("Received Data:", data)

    current = random.uniform(0.1, 0.2)  # 100-200mA
    voltage = 3.3
    energy = voltage * current * 0.1

    latency = time.time() - start_time
    data_size = len(str(data))
    bandwidth = data_size / latency if latency > 0 else 0

    response = {
        "status": "success",
        "message": "Data received successfully!",
        "latency": latency,
        "bandwidth": bandwidth,
        "energy_usage": energy,
        "delay": latency,
        "throughput": data_size / latency,
        "idle_time": 2.0 - latency
    }

    return jsonify(response)
