---
title: Docusaurus
homepage: https://docusaurus.io/en/

description: Docusaurus makes it easy to maintain Open Source documentation websites.

intro: |
    Docusaurus is a static site generator designed specifically for
    documentation websites. It includes pre-configured support for
    localization and versioning, and has built-in support for Algolia-powered
    search.

language:
  name: JavaScript
  link: https://nodejs.org/en/
  icon: devicon-javascript-plain colored

templating:
  name: React
  link: https://reactjs.org/

features:
  localization:
    link: https://docusaurus.io/docs/en/translation
  versioning:
    link: https://docusaurus.io/docs/en/versioning
  custom_output: false
  asset_pipelines: false
  data_files: false
  image_processing: false
  extensible: false

license:
  name: MIT
  slug: mit

adoc: false
md: true
rst: false

twitter: docusaurus
repo: facebook/docusaurus
---

## Markup

Docusaurus has native support for Markdown through the (CommonMark-compliant)
[`remarkable`][1] library.

{{% chart-tabs %}}

[1]: https://github.com/jonschlinkert/remarkable
