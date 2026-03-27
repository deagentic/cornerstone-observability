# Observability Service

Central telemetry microservice for DeAcero Agentic CI infrastructure.
See [ADR-0001](../../docs/adr/ADR-0001-observability-system.md) for the architectural decision.

---

## Quick Start

```bash
# 1. Copy and populate secrets
cp .env.example .env
# Edit .env — set POSTGRES_PASSWORD and DASHBOARD_PASSWORD

# 2. Start the stack
docker compose up -d

# 3. Verify
curl http://localhost:8000/health
```

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `POSTGRES_DB` | yes | Database name |
| `POSTGRES_USER` | yes | Database user |
| `POSTGRES_PASSWORD` | **yes — fail-fast** | Database password. `docker compose` will refuse to start without it. |
| `DASHBOARD_USERNAME` | recommended | HTTP Basic Auth username for dashboard. Leave empty to disable auth (local dev only). |
| `DASHBOARD_PASSWORD` | recommended | HTTP Basic Auth password for dashboard. |

---

## Security Requirements (ADR-0007)

### TLS / HTTPS — MANDATORY for any network-exposed deployment

The observability service listens on HTTP internally (port 8000).
**You MUST place a TLS-terminating reverse proxy in front of it before exposing the service to any network.**

Recommended options for VPS/container deployments:

**nginx + Let's Encrypt (Certbot)**

```nginx
server {
    listen 443 ssl;
    server_name your-observability-host;

    ssl_certificate     /etc/letsencrypt/live/your-host/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-host/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

**Caddy (automatic HTTPS)**

```
your-observability-host {
    reverse_proxy localhost:8000
}
```

> Without TLS, CI metadata (commit SHAs, branch refs, project names) is transmitted
> in plaintext. This violates CICD-SEC-7 and A02:2021 (Cryptographic Failures).

### HTTP Basic Auth — enabled via environment variables

Set `DASHBOARD_USERNAME` and `DASHBOARD_PASSWORD` in `.env`.
When both are non-empty, all dashboard and query API routes require valid credentials.

> For production, prefer a hardened reverse proxy (nginx auth_basic, GCP IAP, or
> similar) over application-level Basic Auth. See ADR-0007 F7.

---

## Endpoints

| Path | Auth required | Description |
|---|---|---|
| `GET /health` | No | Liveness probe |
| `POST /v1/events` | No | Ingest telemetry event |
| `GET /v1/query` | Yes (if configured) | Query stored events |
| `GET /` | Yes (if configured) | HTML dashboard |
