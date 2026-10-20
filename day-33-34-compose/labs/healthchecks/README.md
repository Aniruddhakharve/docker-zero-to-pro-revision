# Lab: healthchecks + depends_on condition

```bash
cp .env.example .env
docker compose -p d3334-health up -d
docker compose -p d3334-health logs app
```

`depends_on` with `condition: service_healthy` delays app start until MySQL healthcheck passes.

Scaling caveat example:

```bash
# This lab has no published app port, but if a service uses fixed host port,
# scaling can fail due to host-port conflict.
docker compose -p d3334-health up -d --scale app=2
```
