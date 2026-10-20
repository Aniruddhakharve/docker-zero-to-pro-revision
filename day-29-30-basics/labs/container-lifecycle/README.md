# Lab: container lifecycle

```bash
docker create --name d2930-ubuntu ubuntu:24.04 sleep infinity
docker start d2930-ubuntu
docker pause d2930-ubuntu
docker unpause d2930-ubuntu
docker exec -it d2930-ubuntu bash
docker restart d2930-ubuntu
docker stop d2930-ubuntu
docker start d2930-ubuntu
docker kill d2930-ubuntu
docker rm d2930-ubuntu
```

Use `docker ps -a` after each step to observe state transitions.
