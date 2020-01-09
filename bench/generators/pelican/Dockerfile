FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-pelican:latest .
# $ docker run --rm hyperfine-pelican 25

# Install Pelican and its dependencies
RUN apk add --no-cache --update \
    asciidoctor \
    && pip3 install pelican Markdown

COPY meta.yml /meta.yml
COPY example_site /example_site

ENTRYPOINT ["python3", "/bench.py"]
