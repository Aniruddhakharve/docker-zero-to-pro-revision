# Lab: named-volume persistence

```bash
docker compose -p d32-volume up -d
docker compose -p d32-volume exec writer cat /data/persist.txt
docker compose -p d32-volume down
docker compose -p d32-volume up -d
docker compose -p d32-volume exec writer cat /data/persist.txt
```

Data persists because it is in named volume `d32_named_data`.
