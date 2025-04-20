from flask import Flask, request, jsonify
import time
import random
import os

app = Flask(__name__)

@app.route('/sensor_data', methods=['POST'])
def receive_data():
    start_time = time.time()
    data = request.get_json()

    print("Received Data:", data)

    # Extract protocol (simulate HTTP/3, MQTT, etc.)
    protocol = data.get("protocol", "http1")

    # Simulated energy usage model
    current = random.uniform(0.1, 0.2)  # in Amps
    voltage = 3.3  # in Volts
    time_active = 0.1  # seconds (100ms active)
    energy = voltage * current * time_active  # Energy in Joules

    # Metrics
    latency = time.time() - start_time
    data_size = len(str(data))  # Approximate data size in bytes
    bandwidth = data_size / latency if latency > 0 else 0  # Bytes/sec
    throughput = data_size / latency
    delay = latency
    idle_time = 2.0 - latency if latency < 2.0 else 0.0

    # Save log
    log_line = f"{time.time()},{protocol},{latency},{bandwidth},{throughput},{energy},{idle_time},{data_size}\n"
    with open("log.csv", "a") as f:
        f.write(log_line)

    # Send response
    response = {
        "status": "success",
        "latency": latency,
        "bandwidth": bandwidth,
        "energy_usage": energy,
        "delay": delay,
        "throughput": throughput,
        "idle_time": idle_time
    }

    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
