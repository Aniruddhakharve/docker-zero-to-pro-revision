FROM golang:1.23-alpine
WORKDIR /src
COPY main.go ./main.go
RUN go build -o /usr/local/bin/d35-single main.go
CMD ["/usr/local/bin/d35-single"]
