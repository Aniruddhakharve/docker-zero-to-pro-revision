# Day 33–34: Docker Compose

## Learning objectives

- Build and run multi-service labs with Compose v2.
- Understand `build` vs `image` usage patterns.
- Use env interpolation, healthchecks, labels, restart policy, and scaling safely.

## Labs

- `labs/compose-basics`
- `labs/app-db`
- `labs/healthchecks`

## Compose v2 commands used

- `docker compose up`, `up -d`
- `docker compose ps`
- `docker compose logs -f`
- `docker compose exec <service> <cmd>`
- `docker compose stop`, `start`
- `docker compose down`, `down -v`

## Run labs

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-33-34-compose/labs/compose-basics
docker compose -p d3334-basic up -d --build
docker compose -p d3334-basic ps
docker compose -p d3334-basic logs -f
```

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-33-34-compose/labs/app-db
cp .env.example .env
docker compose -p d3334-appdb up -d
docker compose -p d3334-appdb exec app sh -c 'wget -qO- http://localhost:8080 | head -n 3'
```

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-33-34-compose/labs/healthchecks
cp .env.example .env
docker compose -p d3334-health up -d
docker compose -p d3334-health logs app
```

## Expected behavior

- Compose-basics builds local image and serves custom text.
- App-db services communicate using service DNS names.
- Healthchecks lab shows app waiting for healthy MySQL.

## Important notes

- `depends_on` controls start order, not readiness, unless combined with health conditions.
- Scaling services with fixed host-port mappings can fail (`port already allocated`).
- Use `docker compose -p <name>` to isolate labs.

## Cleanup

```bash
docker compose -p d3334-basic down
docker compose -p d3334-appdb down -v
docker compose -p d3334-health down -v
```

## Quick interview questions

1. Difference between `docker compose down` and `docker compose down -v`?
2. Why does `depends_on` alone not guarantee DB readiness?
3. What happens if you scale a service publishing fixed host port `8080:80`?
