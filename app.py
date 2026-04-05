from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge
import random
import psutil

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Custom metrics for CPU and RAM
cpu_gauge = Gauge('system_cpu_usage_percent', 'Current CPU usage in percent')
ram_gauge = Gauge('system_ram_usage_percent', 'Current RAM usage in percent')
disk_gauge = Gauge('system_disk_usage_percent', 'Current Disk usage in percent')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/data')
def data():
    return jsonify({"value": random.randint(1, 100)})

@app.route('/metrics-summary')
def metrics_summary():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # Update Prometheus gauges
    cpu_gauge.set(cpu)
    ram_gauge.set(ram)
    disk_gauge.set(disk)

    return jsonify({
        "cpu_percent": cpu,
        "memory_percent": ram,
        "disk_percent": disk
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
