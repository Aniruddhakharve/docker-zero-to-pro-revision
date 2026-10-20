# Lab: hello-image

Build and run:

```bash
docker build -t d31-hello-image:1.0 --build-arg APP_VERSION=1.0 .
docker run --rm d31-hello-image:1.0
```

What this shows:

- `FROM`, `ARG`, `ENV`, `WORKDIR`, `COPY`, `ADD`, `RUN`, `USER`, `EXPOSE`, `HEALTHCHECK`, `CMD`
- Why `COPY` is normally preferable to `ADD` for local files
