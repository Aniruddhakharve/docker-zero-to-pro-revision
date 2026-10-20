# Java multi-stage + jlink revision notes

## Why multi-stage helps Java builds

Build stages let you compile/package with Maven in a builder image and copy only runtime artifacts to the final image.

## Why multi-stage alone may not drastically shrink runtime

If runtime still uses a full JDK/JRE base, size savings can be limited. Big dependencies and app artifacts still dominate.

## What `jlink` does

`jlink` builds a custom Java runtime with only required modules. Correct module discovery is critical: missing modules cause runtime failures.

## Non-root runtime users

Run Java/Tomcat process as non-root to reduce privilege and blast radius if compromised.

## Compose fit: DNS, healthchecks, env vars

- App connects to DB using service name (for example `db`).
- DB healthcheck + app `depends_on` condition improves startup reliability.
- Runtime config (DB host/user/password) should come from env vars.

## Build image vs runtime image

- Build image: includes Maven/toolchain; ephemeral.
- Runtime image: only app + runtime dependencies; should be smaller and safer.
