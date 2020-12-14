FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-jekyll:latest .
# $ docker run --rm hyperfine-jekyll 25

COPY meta.yml /meta.yml
COPY example_site /example_site

# Install Jekyll and its dependencies
RUN apk add --update ruby libstdc++ \
    && apk add ruby-etc \
    && apk add --virtual build-dependencies build-base ruby-dev libffi-dev \
    && gem install bundler --no-ri --no-rdoc \
    && bundle install --gemfile=example_site/Gemfile \
    && apk del build-dependencies

ENTRYPOINT ["python3", "/bench.py"]
