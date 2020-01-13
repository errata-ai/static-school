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

{{% chart-formats id="benchmark-ssgs" md="true" adoc="false" rst="false" %}}

As you can see, Eleventy compares well to other SSGs: for Markdown, it's among
the fastest in our test suite. Notably, it's also the fastest JavaScript-based
SSG by decent margin.

[1]: https://github.com/markdown-it/markdown-it
[2]: https://github.com/11ty/eleventy/issues/117
