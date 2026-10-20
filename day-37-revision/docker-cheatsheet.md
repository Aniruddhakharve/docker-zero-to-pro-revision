# Docker cheatsheet

## Containers

- `docker run -d --name web -p 8080:80 nginx:1.27-alpine`
- `docker ps`, `docker ps -a`
- `docker start|stop|restart <container>`
- `docker exec -it <container> sh`
- `docker logs -f <container>`

## Images

- `docker pull <image:tag>`
- `docker images`
- `docker image inspect <image>`
- `docker image history <image>`
- `docker rmi <image>`

## Dockerfiles

- `docker build -t myimg:1.0 .`
- `docker build --no-cache -t myimg:debug .`

## Volumes

- `docker volume ls`
- `docker volume inspect <volume>`
- `docker volume rm <volume>`

## Networks

- `docker network ls`
- `docker network inspect <network>`
- `docker network create mynet`

## Compose

- `docker compose -p lab up -d --build`
- `docker compose -p lab ps`
- `docker compose -p lab logs -f`
- `docker compose -p lab exec <service> sh`
- `docker compose -p lab down`
- `docker compose -p lab down -v`

## Registries

- `docker login`
- `docker tag local:1.0 user/local:1.0`
- `docker push user/local:1.0`
- `docker pull user/local:1.0`

## Inspection

- `docker inspect <container-or-image>`
- `docker port <container>`
- `docker top <container>`

## Cleanup (careful)

- `docker system df`
- `docker container prune`
- `docker image prune`
- `docker volume prune`
- `docker system prune -a --volumes`
