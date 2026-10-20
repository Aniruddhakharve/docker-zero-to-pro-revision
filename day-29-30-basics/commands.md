# Day 29–30 command reference

> Run commands intentionally. Commands under **destructive cleanup** can delete data.

## 1) Running and listing containers

- `docker run hello-world` — run test container once.
- `docker run -d --name web -p 18080:80 nginx:1.27-alpine` — run Nginx detached.
- `docker run -it --name shell ubuntu:24.04 bash` — interactive shell.
- `docker ps` — running containers.
- `docker ps -a` — running + stopped containers.

## 2) Lifecycle operations

- `docker create --name demo ubuntu:24.04 sleep infinity` — create without start.
- `docker start demo` / `docker stop demo`
- `docker restart demo`
- `docker pause demo` / `docker unpause demo`
- `docker kill demo` — force stop (SIGKILL).
- `docker rm demo` — remove stopped container.
- `docker rm -f demo` — force remove running container.

## 3) Inspecting containers

- `docker inspect demo` — full JSON config/state.
- `docker inspect -f '{{.NetworkSettings.IPAddress}}' demo` — IP on default bridge.
- `docker port web` — mapped ports.
- `docker logs web` / `docker logs -f web` — logs and follow mode.
- `docker exec -it demo bash` — run command in running container.

## 4) Images and layers

- `docker pull alpine:3.20` — download image.
- `docker images` — list local images.
- `docker image inspect alpine:3.20`
- `docker image history alpine:3.20` — layer history.

## 5) Exited vs deleted containers

- Exited container: still exists (`docker ps -a`), metadata and writable layer remain.
- Deleted container: removed via `docker rm`; writable layer is gone.

## 6) Disk usage and cleanup

- `docker system df` — disk usage overview.
- `docker image prune` — remove dangling images only.
- `docker container prune` — remove all stopped containers.
- `docker volume prune` — remove unused volumes.
- `docker system prune` — remove multiple unused objects.
- `docker system prune -a --volumes` — **destructive**: can remove unused images and volumes.

### Safety tip

Always run `docker ps -a`, `docker volume ls`, and `docker system df` before prune commands.
