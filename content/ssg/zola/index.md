---
title: Zola
homepage: https://www.getzola.org/

description: A fast static site generator in a single binary with everything built-in.

intro: |
    Zola is a static site generator that installs as a single executable with
    with "everything built-in" (e.g., Sass compilation, syntax highlighting,
    and TOC generation). It's also one of the fastest static site generators
    available, building most sites in less than a second.

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

Zola supports Markdown through the CommonMark-compliant [pulldown-cmark][1] library.

{{% chart-tabs %}}

[1]: https://github.com/raphlinus/pulldown-cmark
