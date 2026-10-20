# Lab: CMD vs ENTRYPOINT

```bash
# CMD example
docker build -f Dockerfile.cmd -t d31-cmd:1.0 .
docker run --rm d31-cmd:1.0
docker run --rm d31-cmd:1.0 new-value

# ENTRYPOINT example
docker build -f Dockerfile.entrypoint -t d31-entrypoint:1.0 .
docker run --rm d31-entrypoint:1.0
docker run --rm d31-entrypoint:1.0 new-value
```

- CMD gets replaced when you pass command arguments.
- ENTRYPOINT stays fixed; passed args are appended.
