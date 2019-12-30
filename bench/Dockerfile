FROM alpine:3.10

# Usage:
#
# $ docker build -f Dockerfile -t jdkato/hyperfine:latest .
# $ docker tag jdkato/hyperfine:latest jdkato/hyperfine:latest
# $ docker push jdkato/hyperfine

# Install hyperfine:
#
# https://github.com/sharkdp/hyperfine
ARG repo="@testing http://dl-3.alpinelinux.org/alpine/edge/testing"

RUN echo $repo >> /etc/apk/repositories && \
    apk add --no-cache --update hyperfine@testing

COPY corpus /corpus

ENTRYPOINT ["hyperfine"]
