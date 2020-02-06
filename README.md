# Static School [![Netlify Status](https://api.netlify.com/api/v1/badges/ed60bc51-026c-4e4d-b22f-3b16cfc70493/deploy-status)](https://app.netlify.com/sites/festive-wiles-39ebae/deploys) [![PageSpeed](https://img.shields.io/badge/PageSpeed-98%20%2F%20100-success?style=flat&logo=google&logoColor=white)](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fstaticschool.com%2F&tab=desktop) [![Accessibility](https://img.shields.io/badge/accessibility-passing-success?style=flat&logo=html5&logoColor=white)](https://wave.webaim.org/report#/https://staticschool.com/)

Static School is an open-source project with the goal of making it easier to discover, research, and (ultimately) choose a static site generator (SSG) for your next project. We try to provide in-depth analysis for all SSGs we cover, including data (updated daily) on activity, popularity, and performance.

## Site Structure

Static School is built with [Hugo](https://gohugo.io/) and deployed daily with [Netlify](https://www.netlify.com/).

```text
├── LICENSE
├── README.md
├── bench <Files related to data collection and benchmarking>
├── config.toml
├── content
│  └── ssg/ <Individual pages for each SSG>
├── data
│  └── report.json <An auto-generated, JSON-formatted report of all our data>
├── layouts
├── resources
```

## Benchmarking

> **Dependecies**: To run the benchmark suite, you'll need [Python 3.7+](https://www.python.org/downloads/) and [Docker](https://www.docker.com/products/docker-desktop) installed.

Each static site generator is tested against three size increments 10, 100, and 1,000 files. The files are copied from a [corpus](https://github.com/errata-ai/static-school/tree/master/bench/corpus) of approximately-equivalent files for AsciiDoc, Markdown, and reStructuredText.

The following commands will build and run the benchmark suite:

```shell
$ cd bench
$ make build
$ make bench ssg=<NAME OF SSG TO TEST>
```

The actual benchmarking is handled by the [hyperfine](https://github.com/sharkdp/hyperfine) command-line tool, which handles warmup runs, statistical outlier detection, and results formatting.

## Contributing

If you'd like to submit a new static generator to our test suite, please follow these steps:

1. Create a new directory in [`/bench/generators/`][1] that includes `sample_site/`, `Dockerfile`, and `meta.yml`.

   `example_site/` is a functional example of the given static site generator&mdash;it's the template that will be used for all performance testing. When committed to this repo, though, its content directory should be empty.

   `Dockerfile` should contain all required steps to build `example_site/` while adhering to the following structure:

   ```dockerfile
   # Required:
   FROM jdkato/hyperfine

   # Custom steps:
   ARG repo="@testing http://dl-3.alpinelinux.org/alpine/edge/testing"

   RUN echo $repo >> /etc/apk/repositories && \
   apk add --no-cache --update zola@testing

   # Required:
   COPY meta.yml /meta.yml
   COPY example_site /example_site

   # Required:
   ENTRYPOINT ["python3", "/bench.py"]
   ```

   `meta.yml` acts as a means of standardization across multiple static site generators:

   ```yaml
   # All supported formats from 'md', 'adoc', and 'rst':
   formats:
    - md

   # The CLI commands to (1) build the site and (2) obtain the tool's version:
   commands:
    build: 'cd {dir} && zola build && cd ..'
    version: zola --version

   # Any required front matter. This will be added to all test files.
   layout: |
    +++
    title = "Benchmark"
    +++

    {content}

   # The file naming scheme to use for test files:
   filename: test{0}

   # The location, relative to `/example_site`, to copy test markup files:
   content: content
   ```
2. Create a new directory in [`/content/ssg`](https://github.com/errata-ai/static-school/tree/master/content/ssg) that includes `logo.png` (project logo), `preview.png` (website screenshot), and `index.md` (project description and metadata).

   `index.md` should define the following front matter variables (the example below is for [Gatsby](https://www.gatsbyjs.org/)):

   ```yaml
   title: Gatsby
   homepage: https://www.gatsbyjs.org/

   description: Build blazing fast, modern apps and websites with React.

   language:
     name: JavaScript
     link: https://nodejs.org/en/
     icon: devicon-javascript-plain colored

   templating:
     name: React
     link: https://reactjs.org/

   features:
     localization:
       type: plugin
       link: https://www.gatsbyjs.org/docs/localization-i18n/
     versioning: false
     custom_output:
       type: plugin
       link: https://github.com/dominicfallows/gatsby-plugin-json-output
     asset_pipelines:
       type: plugin
       link: https://www.gatsbyjs.org/packages/gatsby-plugin-minify/
     data_files:
       link: https://www.gatsbyjs.org/docs/recipes/sourcing-data
     image_processing:
       link: https://www.gatsbyjs.org/docs/gatsby-image/
     extensible:
       link: https://www.gatsbyjs.org/docs/creating-plugins/

   license:
     name: MIT
     slug: mit

   adoc: true
   md: true
   rst: false

   twitter: gatsbyjs
   repo: gatsbyjs/gatsby
   ```

## Credits

This project was inspired by Netlify's MIT-licensed [StaticGen](https://www.staticgen.com/) website. The major difference is that *Static School* is much more than a "leaderboard": we provide in-depth benchmarking, guides, and tutorials.

[1]: https://github.com/errata-ai/static-school/tree/master/bench/generators
