FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-hugo:latest .
# $ docker run --rm hyperfine-hugo 25

# Install Hugo and its dependencies
RUN apk add --no-cache --update \
    hugo \
    asciidoctor \
    && pip3 install docutils pygments

COPY meta.yml /meta.yml

ENTRYPOINT ["python3", "/bench.py"]
