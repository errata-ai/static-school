FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-zola:latest .
# $ docker run --rm hyperfine-zola 25

# Install Zola and its dependencies
ARG repo="@testing http://dl-3.alpinelinux.org/alpine/edge/community"

RUN echo $repo >> /etc/apk/repositories && \
    apk add --no-cache --update zola@testing

COPY meta.yml /meta.yml
COPY example_site /example_site

ENTRYPOINT ["python3", "/bench.py"]
