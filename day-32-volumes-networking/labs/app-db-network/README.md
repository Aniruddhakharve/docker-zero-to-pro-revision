# Lab: app-db network communication

```bash
docker compose -p d32-appdb up -d
docker compose -p d32-appdb logs app
```

The app reaches DB at hostname `db` (service name), not by container IP.

No DB host port is published because inter-container traffic stays on Docker network.
