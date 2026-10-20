FROM alpine:3.20

ARG APP_VERSION=dev
ENV GREETING="Hello from Dockerfile"     APP_VERSION=${APP_VERSION}

WORKDIR /app
COPY message.txt /app/message.txt
ADD note.txt /app/note.txt

RUN adduser -D appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD test -f /app/message.txt || exit 1

CMD ["sh", "-c", "echo "$GREETING (version: $APP_VERSION)" && cat /app/message.txt"]
