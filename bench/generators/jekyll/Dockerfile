FROM jdkato/hyperfine

COPY meta.yml /meta.yml
COPY Gemfile /Gemfile
COPY base.yml /base.yml

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-jekyll:latest .
# $ docker run --rm hyperfine-jekyll 25

# Install Jekyll and its dependencies
RUN apk add --update ruby libstdc++ \
    && apk add --virtual build-dependencies build-base ruby-dev libffi-dev \
    && gem install bundler --no-ri --no-rdoc \
    && bundle install \
    && gem cleanup \
    && apk del build-dependencies

ENTRYPOINT ["python3", "/bench.py"]
