# Day 32: Volumes and networking

## Learning objectives

- Understand writable-layer data loss.
- Persist data with named volumes.
- Use bind mounts for live host edits.
- Use user-defined bridge networking and container DNS names.

## Labs

- `labs/named-volume`
- `labs/bind-mount`
- `labs/custom-network`
- `labs/app-db-network`

## Run labs

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-32-volumes-networking/labs/named-volume
docker compose -p d32-volume up -d

docker compose -p d32-volume exec writer sh -c 'ls -l /data && cat /data/persist.txt'

docker compose -p d32-volume down
```

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-32-volumes-networking/labs/bind-mount
docker compose -p d32-bind up -d
# edit host file ./site/index.html and refresh http://localhost:18282
```

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-32-volumes-networking/labs/custom-network
docker compose -p d32-net up -d
docker compose -p d32-net exec client ping -c 2 server
```

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-32-volumes-networking/labs/app-db-network
docker compose -p d32-appdb up -d
docker compose -p d32-appdb logs app
```

## Expected behavior

- Named volume keeps data after container recreation.
- Bind mount shows host edits immediately in container.
- Client resolves `server` over custom bridge network.
- App reaches DB using service DNS (`db`).

## Host vs container ports

- `-p 18282:80` means host `18282` forwards to container `80`.
- Containers on same Docker network talk using service/container names without publishing DB port.

## Cleanup

```bash
docker compose -p d32-volume down
docker compose -p d32-bind down
docker compose -p d32-net down
docker compose -p d32-appdb down
# Delete persistence only when intended:
docker compose -p d32-volume down -v
docker compose -p d32-appdb down -v
```

## Common mistakes

- Expecting bind mount changes without saving host file.
- Publishing database ports unnecessarily.
- Forgetting `down -v` removes named volumes.

## Quick interview questions

1. Why does writable-layer data disappear after container deletion?
2. How is a user-defined bridge better than default bridge for service discovery?
3. When do you use bind mount vs named volume?
