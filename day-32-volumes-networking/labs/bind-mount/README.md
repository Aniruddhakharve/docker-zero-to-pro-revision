# Lab: bind-mount

```bash
docker compose -p d32-bind up -d
curl http://localhost:18282
# edit ./site/index.html on host and refresh browser
docker compose -p d32-bind down
```

Bind mounts are ideal for local edit-feedback loops.
