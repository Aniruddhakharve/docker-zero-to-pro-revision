# Day 29–30: Docker fundamentals and lifecycle

## Learning objectives

- Understand image vs container.
- Run, inspect, and manage container lifecycle.
- Inspect images, logs, mounts, and networking.
- Clean up safely without deleting needed data.

## Concepts covered

- Core `docker run` workflows
- Interactive containers
- Lifecycle operations (`start/stop/restart/pause/kill/rm`)
- Container and image inspection
- Exited vs deleted containers
- Disk usage and prune risks

## Labs

- `labs/hello-world`
- `labs/nginx-container`
- `labs/container-lifecycle`

## Run the labs

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-29-30-basics/labs/hello-world
docker run --rm hello-world

cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-29-30-basics/labs/nginx-container
docker run -d --name d2930-nginx -p 18080:80 nginx:1.27-alpine
curl http://localhost:18080
docker rm -f d2930-nginx

cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-29-30-basics/labs/container-lifecycle
docker create --name d2930-ubuntu ubuntu:24.04 sleep infinity
docker start d2930-ubuntu
docker exec -it d2930-ubuntu bash
```

## Expected behavior

- `hello-world` prints a success message.
- Nginx returns default welcome HTML on port `18080`.
- Ubuntu container remains running until stopped.

## Cleanup

```bash
docker rm -f d2930-nginx d2930-ubuntu 2>/dev/null || true
docker container prune  # review prompt before confirming
```

## Common mistakes

- Forgetting host:container order in `-p` (`18080:80`, not `80:18080`).
- Trying `docker exec` on a stopped container.
- Removing a container and expecting writable-layer data to remain.

## Quick interview questions

1. What is the difference between an image and a container?
2. Why might a container be in `Exited` state?
3. What does `docker inspect` give you that `docker ps` does not?
