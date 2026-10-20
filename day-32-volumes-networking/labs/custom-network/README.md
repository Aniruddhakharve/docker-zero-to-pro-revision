# Lab: custom-network and DNS

```bash
docker compose -p d32-net up -d
docker compose -p d32-net exec client ping -c 2 server
docker compose -p d32-net down
```

`client` resolves `server` by service name because both are on `labnet`.
