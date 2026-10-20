# Lab: non-root-user

```bash
docker build -t d35-nonroot:1.0 .
docker run --rm d35-nonroot:1.0
```

Expected output UID should not be `0`.
