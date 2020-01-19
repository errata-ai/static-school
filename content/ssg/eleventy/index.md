---
title: Eleventy
homepage: https://www.11ty.dev/

description: A simpler static site generator.

intro: |
    Eleventy is a "simpler static site generator" that was created to be a
    JavaScript alternative to the Ruby-based Jekyll. It's
    ["zero config"](https://www.11ty.dev/docs/resources/#zero-config) by
    default and doesn't require a particular directory structure.

language:
  name: JavaScript
  link: https://nodejs.org/en/
  icon: devicon-javascript-plain colored

templating:
  name: Nunjucks
  link: https://mozilla.github.io/nunjucks/templating.html

features:
  localization: false
  versioning: false
  custom_output: false
  asset_pipelines:
    type: plugin
    link: https://github.com/philhawksworth/eleventyone
  data_files:
    link: https://www.11ty.dev/docs/data/
  image_processing:
    type: plugin
    link: https://github.com/eeeps/eleventy-respimg#readme
  extensible:
    link: https://www.11ty.dev/docs/plugins/

localization: false
versioning: false
theming: true

license:
  name: MIT
  slug: mit

adoc: false
md: true
rst: false

twitter: eleven_ty
repo: 11ty/eleventy
---

## Markup

Eleventy has native support for Markdown through the (CommonMark-compliant)
[`markdown-it`][1] library. It currently doesn't support any other format, but
there is discussion about adding [Custom File Extension Handlers][2].

{{% chart-tabs %}}

[1]: https://github.com/markdown-it/markdown-it
[2]: https://github.com/11ty/eleventy/issues/117
