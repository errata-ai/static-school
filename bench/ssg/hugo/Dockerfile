FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-hugo:latest .
# $ docker run --rm hyperfine-hugo 25

# Install Hugo and its dependencies
RUN apk add --no-cache --update \
    hugo \
    asciidoctor \
    python3 \
    && pip3 install docutils pygments

COPY bench.py /bench.py

ENTRYPOINT ["python3", "/bench.py"]
