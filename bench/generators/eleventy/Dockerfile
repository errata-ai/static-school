FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-eleventy:latest .
# $ docker run --rm hyperfine-eleventy 25

COPY meta.yml /meta.yml
COPY example_site /example_site

# Install 11ty and its dependencies
RUN apk add --no-cache --update npm \
    && npm install -g @11ty/eleventy yarn \
    && yarn install --cwd example_site

ENTRYPOINT ["python3", "/bench.py"]
