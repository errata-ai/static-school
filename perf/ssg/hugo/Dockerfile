FROM jdkato/hyperfine

# Usage:
#
# $ docker build -f Dockerfile -t hyperfine-hugo:latest .
# $ docker run --rm hyperfine-hugo

# Install Hugo and its dependencies
RUN apk add --no-cache --update \
    hugo \
    asciidoctor \
    && pip3 install docutils

COPY layout.txt /layout.txt
COPY entrypoint.sh /entrypoint.sh

# Create our testing sites:

# AsciiDoc
RUN hugo new site adoc
RUN cd adoc && hugo new post/test.adoc && cd -

# Markdown
RUN hugo new site md
RUN cd md && hugo new post/test.md && cd -

# reStructuredText
RUN hugo new site rst
RUN cd rst && hugo new post/test.rst && cd -

# Build the benchmarking corpus:
RUN python3 /main.py /layout.txt {0}/content/post/{1} 25

ENTRYPOINT ["/entrypoint.sh"]
