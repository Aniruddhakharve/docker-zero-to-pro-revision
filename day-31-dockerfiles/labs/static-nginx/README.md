# Lab: static-nginx

```bash
docker build -t d31-static-nginx:1.0 .
docker run --rm -p 18181:80 d31-static-nginx:1.0
curl http://localhost:18181
```
