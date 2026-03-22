# Flask Monitoring Stack

A containerized REST API with a full observability stack.

## Tech Stack
- Python Flask - REST API
- Docker & Docker Compose - Containerization
- Prometheus - Metrics collection
- Grafana - Metrics visualization

## Features
- REST API with /health and /data endpoints
- Real-time request monitoring
- Grafana dashboard showing request rates and status codes

## How to Run
```bash
docker-compose up --build
```

Then visit:
- Flask API: http://localhost:5000/health
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Architecture
Flask App → Prometheus (scrapes metrics every 15s) → Grafana (visualizes data)