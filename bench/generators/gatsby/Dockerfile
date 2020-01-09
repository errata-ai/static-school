FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-gatsby:latest .
# $ docker run --rm hyperfine-gatsby 25

COPY meta.yml /meta.yml
COPY example_site /example_site

# Install gatsby and its dependencies
#
# TODO: Benchmark AsciiDoc
RUN apk add --no-cache --update npm \
    && npm install -g gatsby-cli yarn \
    && yarn install --cwd example_site

ENTRYPOINT ["python3", "/bench.py"]
