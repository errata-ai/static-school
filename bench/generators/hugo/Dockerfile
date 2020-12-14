FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-hugo:latest .
# $ docker run --rm hyperfine-hugo 25

ARG repo="@testing http://dl-3.alpinelinux.org/alpine/edge/community"

# Install Hugo and its dependencies
RUN apk add --no-cache --update \
    hugo \
    asciidoctor \
    && pip3 install docutils pygments

COPY meta.yml /meta.yml
COPY example_site /example_site

ENTRYPOINT ["python3", "/bench.py"]
