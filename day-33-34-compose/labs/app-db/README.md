# Lab: app-db (prebuilt images with env vars)

```bash
cp .env.example .env
docker compose -p d3334-appdb up -d
docker compose -p d3334-appdb ps
```

Open `http://localhost:18302` (Adminer). Server name is `db`.

This lab demonstrates:

- Using `image` for prebuilt images
- `.env` interpolation in Compose
- Service-name DNS (`db`)
- Named volume persistence
