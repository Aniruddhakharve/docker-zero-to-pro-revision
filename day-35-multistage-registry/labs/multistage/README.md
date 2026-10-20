# Lab: multistage

```bash
docker build -t d35-multistage:1.0 .
docker run --rm d35-multistage:1.0
```

Inspect:

```bash
docker image history d35-single:1.0
docker image history d35-multistage:1.0
docker image inspect d35-multistage:1.0 --format '{{.Id}}'
```
