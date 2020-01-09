---
title: Zola
homepage: https://www.getzola.org/

description: A fast static site generator in a single binary with everything built-in.

language:
  name: Rust
  link: https://www.rust-lang.org/

templating:
  name: Tera
  link: https://tera.netlify.com/

localization: false
versioning: false
theming: true

license:
  name: MIT
  slug: mit

adoc: false
md: true
rst: false

twitter: getzola/zola
repo: getzola/zola
---

## Markup

Zola supports Markdown through the CommonMark-compliant [pulldown-cmark][1] library. Zola makes up for *only* supporting Markdown by being of the fastest generators in our test suite.

{{% chart id="benchmark-formats" %}}

As you can see, Zola is capable of building a 1,000-file site **in around 1 second**.

{{% chart-formats id="benchmark-ssgs" md="true" adoc="false" rst="false" %}}

Compared to other generators, only Hugo is able to match Zola's performance and both were neck-and-neck at every size increment.

## Templating

Coming soon.

## Localization (i18n)

Coming soon.

## Versioning

Coming soon.

## Theming

Coming soon.

## Language

Coming soon.

[1]: https://github.com/raphlinus/pulldown-cmark
