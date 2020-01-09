FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-hexo:latest .
# $ docker run --rm hyperfine-hexo 25

COPY meta.yml /meta.yml
COPY example_site /example_site

# Install Hexo and its dependencies
RUN apk add --no-cache --update \
    git \
    npm \
    && npm install -g hexo-cli yarn \
    && yarn install --cwd example_site

ENTRYPOINT ["python3", "/bench.py"]
