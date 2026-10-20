# Day 35: Multi-stage builds, hardening, and image distribution

## Learning objectives

- Compare single-stage and multi-stage builds.
- Use named stages and `COPY --from`.
- Run containers as non-root user.
- Understand tags, IDs, digests, and registry basics.

## Labs

- `labs/single-stage`
- `labs/multistage`
- `labs/non-root-user`
- `labs/image-tagging`

## Run labs

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-35-multistage-registry/labs/single-stage
docker build -t d35-single:1.0 .
docker run --rm d35-single:1.0

cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-35-multistage-registry/labs/multistage
docker build -t d35-multistage:1.0 .
docker run --rm d35-multistage:1.0
```

## Concepts

- Single-stage keeps build tools in final image.
- Multi-stage copies only final artifact to runtime stage.
- Smaller images reduce pull time and attack surface.
- Prefer pinned tags (`python:3.12-slim`) over floating (`latest`).

## Base image trade-offs

- **alpine**: small, musl-based; some binaries may behave differently.
- **slim**: larger than alpine but broader compatibility.
- **distroless**: minimal runtime, no shell/package manager.
- **scratch**: empty base, only for fully static binaries.

## Registry actions (optional)

Core lessons do not require registry accounts.

```bash
# optional
docker login
docker tag d35-multistage:1.0 <your-user>/d35-multistage:1.0
docker push <your-user>/d35-multistage:1.0
docker pull <your-user>/d35-multistage:1.0
```

## Cleanup

```bash
docker image rm d35-single:1.0 d35-multistage:1.0 d35-nonroot:1.0 2>/dev/null || true
```

## Quick interview questions

1. Why use `COPY --from=builder`?
2. Why avoid running as root in runtime containers?
3. Difference between tag and digest?
