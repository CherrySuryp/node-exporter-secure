# Node Exporter Secure
This is a custom API written with FastAPI Python framework that forwards [Prometheus Node-Exporter](https://github.com/prometheus/node_exporter) metrics data over secured endpoint with Bearer Auth

## Installation
### Docker-Compose
  Fully complete `docker-compose.yml` ready to deploy, you only need to update `API_BEARER_TOKEN` env variable
```yaml
name: node-exporter-secure
services:
  node-exporter:
      image: quay.io/prometheus/node-exporter:latest
      container_name: node-exporter
      command:
        - '--path.rootfs=/host'
      pid: host
      restart: unless-stopped
      volumes:
        - /:/host:ro,rslave

  api:
    image: abelodev/node-exporter-secure:latest
    container_name: node-exporter-secure
    environment:
      API_BEARER_TOKEN: "token"
    command: ["sh", "-c", "uvicorn app.main:app --host=0.0.0.0 --port=8000"]
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://node-exporter-secure:8000/debug/healthcheck"]
      interval: 1m
      timeout: 10s
    ports:
      - "9100:8000"
    depends_on:
      - node-exporter

```

## Environment Variables
- `ENV` - `DEV` or `PROD`. Production env disables `/docs`, `/redoc` and `/openapi.json` endpoints. `PROD` is set by default.
- `API_BEARER_TOKEN` - Your Bearer token auth
- `METRICS_ROUTE` - Metrics route. Default set to `/metrics`
- `NODE_EXPORTER_METRICS_PATH` - Node-Exporter endpoint path. Default set to `http://node-exporter:9100/metrics`
