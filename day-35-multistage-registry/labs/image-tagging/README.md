# Lab: image-tagging and registry references

Use an existing image to practice tags, IDs, and digests:

```bash
docker pull nginx:1.27-alpine
docker images nginx

docker tag nginx:1.27-alpine d35-nginx-lab:1.27
docker tag nginx:1.27-alpine d35-nginx-lab:stable

docker image inspect d35-nginx-lab:1.27 --format '{{.Id}}'
docker image inspect nginx:1.27-alpine --format '{{index .RepoDigests 0}}'
```

- Tags are mutable labels.
- Image ID is local immutable content ID.
- Digest identifies pushed content in registry.
