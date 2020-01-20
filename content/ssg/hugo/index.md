---
title: Hugo
homepage: https://gohugo.io/

description: The world’s fastest framework for building websites.

intro: |
    Hugo is a fast ("less than 1 ms per page"), self-contained static site
    generator. Its native binary includes most of its features out-of-the-box,
    allowing you to avoid having install plugins and dependencies.

language:
  name: Go
  link: https://golang.org/
  icon: devicon-go-line colored

templating:
  name: Go
  link: https://gohugo.io/templates/introduction/

features:
  localization:
    type: native
    link: https://gohugo.io/content-management/multilingual/
  versioning: false
  # NOTE:
  #
  # https://discourse.gohugo.io/t/documentation-site-versioning/5898/9
  # https://github.com/dgraph-io/dgraph/tree/master/wiki
  custom_output:
    link: https://gohugo.io/templates/output-formats/
  asset_pipelines:
    link: https://gohugo.io/hugo-pipes/introduction/
  data_files:
    link: https://gohugo.io/templates/data-templates/
  image_processing:
    link: https://gohugo.io/content-management/image-processing/
  extensible: false

license:
  name: Apache 2.0
  slug: apache-2

adoc: true
md: true
rst: true

twitter: GoHugoIO
repo: gohugoio/hugo
---

## Markup

Hugo has native support for Markdown (standards-compliant), and supports AsciiDoc and reStructuredText through [external libraries][1].

{{% chart-tabs %}}

[1]: https://gohugo.io/content-management/formats/#list-of-content-formats
