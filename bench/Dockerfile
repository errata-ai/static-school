FROM alpine:3.12

# Usage:
#
# $ docker build -f Dockerfile -t jdkato/hyperfine:latest .
# $ docker tag jdkato/hyperfine:latest jdkato/hyperfine:latest
# $ docker push jdkato/hyperfine

# Install hyperfine:
#
# https://github.com/sharkdp/hyperfine
ARG repo="@testing http://dl-3.alpinelinux.org/alpine/edge/community"

RUN echo $repo >> /etc/apk/repositories && \
    apk add --no-cache --update hyperfine@testing py3-pip && \
    pip3 install pyyaml

COPY corpus /corpus
COPY scripts/bench.py /bench.py

ENTRYPOINT ["hyperfine"]
