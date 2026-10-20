# Lab: Nginx with port mapping

```bash
docker run -d --name d2930-nginx -p 18080:80 nginx:1.27-alpine
curl http://localhost:18080
docker rm -f d2930-nginx
```

- Host port `18080` maps to container port `80`.
- Change host port if `18080` is busy: `-p 28080:80`.
