# Day 37: Revision and self-assessment

## Learning objectives

- Rapidly revise Docker commands and concepts.
- Evaluate readiness through conceptual and practical checks.
- Identify weak areas and map them back to earlier labs.

## Concepts covered

- Containers, images, Dockerfiles, volumes, networks, Compose, registries
- Troubleshooting startup, networking, and persistence issues
- CI/CD image integrity pattern (build once, scan same image, deploy same image)

## Files

- `docker-cheatsheet.md`
- `self-assessment.md`

## Run/usage commands

```bash
cd /home/runner/work/docker-zero-to-pro-revision/docker-zero-to-pro-revision/day-37-revision
cat docker-cheatsheet.md
cat self-assessment.md
```

## Expected behavior

- You can execute core Docker/Compose commands from memory.
- You can answer conceptual questions before checking the answer key.
- You can troubleshoot common startup and port-conflict issues.

## Cleanup

No dedicated containers/images are created in this day. Use cleanup from previous day labs as needed.

## Common mistakes and troubleshooting tips

- Reading answer key before attempting questions.
- Memorizing commands without understanding image/container/network scope.
- Ignoring volume impact when using `down -v`.

## Quick interview questions

1. What practical difference exists between tag and digest during deployments?
2. Why does a container stop immediately after its main process exits?
3. How would you debug app startup racing database readiness?

Use:

- [docker-cheatsheet.md](./docker-cheatsheet.md) for command revision.
- [self-assessment.md](./self-assessment.md) to test concepts from beginner to advanced.

Suggested flow:

1. Attempt self-assessment without notes.
2. Check answer key section.
3. Re-run weak labs from earlier days.
