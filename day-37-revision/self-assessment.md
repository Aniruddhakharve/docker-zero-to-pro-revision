# Self-assessment

## Questions (attempt first)

1. Explain image vs container in your own words.
2. Why does writable-layer data disappear after `docker rm`?
3. Compare `CMD` and `ENTRYPOINT` with one command example each.
4. When should you use `COPY` instead of `ADD`?
5. Difference between `EXPOSE` and `-p` at runtime?
6. Default bridge vs user-defined bridge: key differences?
7. How does Compose service-name DNS work?
8. Why is `depends_on` not enough for DB readiness?
9. What is the difference between `docker compose down` and `down -v`?
10. Single-stage vs multi-stage build: when and why?
11. Why run containers as non-root?
12. Distinguish image tags, IDs, and digests.
13. List 3 reasons a container exits quickly.
14. How would you troubleshoot an app starting before DB is ready?
15. Why is build-once/scan-same-image/push-same-image valuable?

## Command exercises

1. Run Nginx on host port `19080` and verify response.
2. Create a container without starting it, then start and inspect it.
3. Build an image with tag `revision:test` from a Dockerfile lab.
4. Create a named volume, write data, remove container, verify persistence.
5. Bring up a Compose app with custom project name `revision-lab`.

## Troubleshooting scenarios

1. `bind: address already in use` when starting a service.
2. App logs show `connection refused` to DB on startup.
3. Container keeps restarting in Compose.
4. Image build is unexpectedly slow after tiny source change.

---

## Answer key / explanations

1. Image is immutable template; container is runnable instance with writable layer.
2. Writable layer belongs to container lifecycle; `docker rm` deletes it. Use volumes for persistence.
3. CMD provides default command/args; ENTRYPOINT fixes executable and usually appends args.
4. Use COPY for simple local file copy; ADD only when its extra features are explicitly needed.
5. EXPOSE is metadata/docs; `-p host:container` publishes port to host.
6. User-defined bridge adds automatic DNS between containers and better isolation controls.
7. Services on same Compose network resolve each other by service name (for example `db`).
8. `depends_on` starts order, not readiness; add healthcheck and `condition: service_healthy`.
9. `down` keeps named volumes; `down -v` removes them too.
10. Multi-stage removes build tools from final runtime image, usually reducing size and attack surface.
11. Non-root reduces privilege and impact of compromise.
12. Tag is mutable label, ID is local immutable content ID, digest is registry content reference.
13. Main process ends, startup command fails, missing dependency/config.
14. Inspect logs/events, verify network DNS, test DB healthcheck, delay app until DB healthy.
15. It prevents drift: security scan, pushed artifact, and deployed artifact are exactly the same image.
