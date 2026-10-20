# docker-zero-to-pro-revision

Hands-on Docker revision lab for Day 29–37 of the 90 Days of DevOps plan. This repo is designed for quick restart after a learning gap: small labs, isolated resources, and practical commands.

## Learning goals

- Rebuild Docker fundamentals (images, containers, lifecycle, inspection).
- Practice Dockerfiles and build strategy (cache, CMD/ENTRYPOINT, multi-stage).
- Master persistence and networking with volumes, bridges, and DNS.
- Use Docker Compose safely with healthchecks, env vars, and project isolation.
- Review CI/CD image flow patterns and Java jlink runtime concepts.

## Prerequisites

- Docker Engine running
- Docker Compose v2 plugin available

Check locally:

```bash
docker version
docker info
docker compose version
```

## Day 29–37 roadmap

- [Day 29–30 Basics](./day-29-30-basics/README.md)
- [Day 31 Dockerfiles](./day-31-dockerfiles/README.md)
- [Day 32 Volumes + Networking](./day-32-volumes-networking/README.md)
- [Day 33–34 Compose](./day-33-34-compose/README.md)
- [Day 35 Multi-stage + Registry](./day-35-multistage-registry/README.md)
- [Day 36 Project Patterns](./day-36-project-patterns/README.md)
- [Day 37 Revision](./day-37-revision/README.md)

## Directory guide

```text
.
├── day-29-30-basics/
├── day-31-dockerfiles/
├── day-32-volumes-networking/
├── day-33-34-compose/
├── day-35-multistage-registry/
├── day-36-project-patterns/
└── day-37-revision/
```

Each day folder contains independent labs with local run/cleanup commands.

## Run labs independently

1. Open the day/lab README.
2. `cd` into the exact lab directory.
3. Run the documented commands.
4. Stop and clean only that lab’s resources.

## Resource isolation strategy

- Each Compose lab uses its own project name in commands (for example `-p d3334-basic`).
- Labs use unique image tags.
- Host ports are unique and/or variable (`${PORT}` style).
- No hard-coded `container_name` in Compose labs.

## Cleanup guidance

- Safe cleanup by lab: `docker compose -p <name> down`
- Remove lab volumes only when intended: `docker compose -p <name> down -v`
- Review disk usage first: `docker system df`
- Treat prune commands as destructive; review targets before using them.

## Progress checklist

- [ ] Day 29–30 fundamentals completed
- [ ] Day 31 Dockerfiles completed
- [ ] Day 32 volumes/networking completed
- [ ] Day 33–34 Compose completed
- [ ] Day 35 multi-stage + registry completed
- [ ] Day 36 project patterns completed
- [ ] Day 37 revision completed

## Important reminder

Run commands from the relevant lab directory and understand each command before executing it.
