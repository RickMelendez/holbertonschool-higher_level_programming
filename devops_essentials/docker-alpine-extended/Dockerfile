FROM alpine:latest

RUN apk add --no-cache curl

COPY config.txt /app/config.txt

RUN chmod 644 /app/config.txt

CMD ["sh"]
