from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/health')
def health():
    return jsonify({"status" : "healthy"})

@app.route('/data')
def data():
    return jsonify({"value" : random.randint(1,100)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)