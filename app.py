from flask import Flask, request, jsonify
import time
import random
import os  # Add this line

app = Flask(__name__)

@app.route('/sensor_data', methods=['POST'])
def receive_data():
    start_time = time.time()
    data = request.get_json()
    print("Received Data:", data)

    current = random.uniform(0.1, 0.2)
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # <- NEW: use PORT from environment
    app.run(host="0.0.0.0", port=port)
