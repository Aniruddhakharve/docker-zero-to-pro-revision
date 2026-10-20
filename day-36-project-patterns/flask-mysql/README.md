# Flask + MySQL pattern lab

Minimal learning lab inspired by secure CI/CD pipeline structure.

## Run with local build (no registry required)

```bash
cp .env.example .env
docker compose -f compose.yaml -f compose.build.yaml -p d36-flask up -d --build
curl http://localhost:18500
```

## Run with prebuilt image pattern

```bash
# IMAGE_TAG can point to an already built/pushed image tag
docker compose -f compose.yaml -p d36-flask up -d
```

## Why `down` vs `down -v` matters

- `docker compose down` removes containers/networks only.
- `docker compose down -v` also removes `d36_mysql_data` volume (DB data loss).

## GitHub SHA vs Compose variables

- `${{ github.sha }}` is evaluated in GitHub Actions workflow YAML.
- `${IMAGE_TAG}` is evaluated by Docker Compose from shell/env/.env.
- CI often sets `IMAGE_TAG=${{ github.sha }}` before running Compose.

## Secure pipeline pattern (concise)

1. Build image once.
2. Scan the exact built image (for example with Trivy).
3. Push that same image/tag.
4. Deploy the same image digest/tag.

Trivy is useful for vulnerability scanning, but not required for this core local lab.

## Cleanup

```bash
docker compose -f compose.yaml -f compose.build.yaml -p d36-flask down
docker compose -f compose.yaml -p d36-flask down -v
```
