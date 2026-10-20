# Day 31: Dockerfiles

## Learning objectives

- Understand core Dockerfile instructions and build context behavior.
- Build minimal images with clear purpose.
- Learn cache-friendly instruction ordering.
- Compare `CMD` and `ENTRYPOINT` behavior.

## Concepts covered

- `FROM`, `WORKDIR`, `COPY`, `ADD`, `RUN`, `ENV`, `ARG`, `EXPOSE`, `USER`, `HEALTHCHECK`, `CMD`, `ENTRYPOINT`
- `.dockerignore` and build context
- Build cache effects

## Labs

- `labs/hello-image`
- `labs/static-nginx`
- `labs/cmd-entrypoint`
- `labs/build-cache`

## Run labs

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-31-dockerfiles/labs/hello-image
docker build -t d31-hello-image:1.0 --build-arg APP_VERSION=1.0 .
docker run --rm d31-hello-image:1.0

cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-31-dockerfiles/labs/static-nginx
docker build -t d31-static-nginx:1.0 .
docker run --rm -p 18181:80 d31-static-nginx:1.0

cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-31-dockerfiles/labs/cmd-entrypoint
docker build -f Dockerfile.cmd -t d31-cmd:1.0 .
docker run --rm d31-cmd:1.0
docker run --rm d31-cmd:1.0 overridden-arg

docker build -f Dockerfile.entrypoint -t d31-entrypoint:1.0 .
docker run --rm d31-entrypoint:1.0
docker run --rm d31-entrypoint:1.0 overridden-arg
```

## Expected behavior

- `hello-image` prints configured env + file content.
- `static-nginx` serves custom HTML.
- CMD image fully replaces default command when args are provided.
- ENTRYPOINT image keeps executable and appends args.

## Cleanup

```bash
docker image rm d31-hello-image:1.0 d31-static-nginx:1.0 d31-cmd:1.0 d31-entrypoint:1.0 d31-cache:1.0 2>/dev/null || true
```

## Common mistakes

- Building from wrong context directory.
- Expecting `ADD` to be mandatory (prefer `COPY` for local files).
- Confusing `EXPOSE` with host publishing (`-p`).

## Quick interview questions

1. Why is `COPY` usually preferred over `ADD`?
2. What changes invalidate Docker build cache?
3. How do CMD and ENTRYPOINT interact?
