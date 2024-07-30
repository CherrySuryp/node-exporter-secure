```yaml
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
      - "8000:8000"
    depends_on:
      - node-exporter

```