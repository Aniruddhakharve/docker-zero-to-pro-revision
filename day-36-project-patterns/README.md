# Day 36: Patterns from real projects

## Learning objectives

- Recreate practical structure patterns with minimal examples.
- Understand build-once/scan/push/deploy image flow.
- Relate Java multi-stage + jlink concepts without rebuilding full project.

## Concepts covered

- Flask + MySQL Compose pattern with service DNS and healthchecks
- Prebuilt image deployment pattern vs local build override
- Safe env variable handling with `.env.example`
- Java runtime optimization notes (`jlink`) and non-root runtime practices

## Labs / directories

- `flask-mysql/` runnable mini lab
- `java-jlink-notes/` concise architecture notes

## Run commands

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-36-project-patterns/flask-mysql
cp .env.example .env
docker compose -f compose.yaml -f compose.build.yaml -p d36-flask up -d --build
curl http://localhost:18500
```

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-36-project-patterns/java-jlink-notes
cat README.md
```

## Expected behavior

- Flask endpoint returns JSON with `db_check: 1`.
- MySQL healthcheck turns healthy before Flask starts.
- Notes explain Java build/runtime separation and jlink trade-offs.

## Cleanup

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-36-project-patterns/flask-mysql
docker compose -f compose.yaml -f compose.build.yaml -p d36-flask down
docker compose -f compose.yaml -p d36-flask down -v
```

## Common mistakes and troubleshooting tips

- Using `localhost` for DB host inside container instead of service name `db`.
- Forgetting `.env` values, leading to auth failures.
- Confusing `docker compose down` (keeps volume) with `down -v` (deletes DB volume).

## Quick interview questions

1. Why is build-once/scan-same-image/push-same-image safer than rebuilding later?
2. Why should app containers connect to `db` service name instead of hard-coded IP?
3. What does `jlink` solve in Java runtime images?
