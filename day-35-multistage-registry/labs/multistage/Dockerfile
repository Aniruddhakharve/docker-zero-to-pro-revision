FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY main.go ./main.go
RUN CGO_ENABLED=0 go build -o /out/d35-multi main.go

FROM alpine:3.20 AS runtime
COPY --from=builder /out/d35-multi /usr/local/bin/d35-multi
ENTRYPOINT ["/usr/local/bin/d35-multi"]
