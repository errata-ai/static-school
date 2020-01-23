FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-docusaurus:latest .
# $ docker run --rm hyperfine-docusaurus 25

COPY meta.yml /meta.yml
COPY example_site /example_site

# Install Docusaurus and its dependencies
RUN apk add --no-cache \
    autoconf \
    automake \
    bash \
    g++ \
    libc6-compat \
    libjpeg-turbo-dev \
    libpng-dev \
    make \
    nasm

RUN apk add --no-cache --update npm \
    && npm install -g yarn \
    && yarn install --cwd example_site/website

ENTRYPOINT ["python3", "/bench.py"]
