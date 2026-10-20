# Lab: compose-basics

```bash
docker compose -p d3334-basic up -d --build
docker compose -p d3334-basic ps
docker compose -p d3334-basic logs -f web
docker compose -p d3334-basic exec web ls -l /usr/share/nginx/html
docker compose -p d3334-basic stop
docker compose -p d3334-basic start
docker compose -p d3334-basic down
```
