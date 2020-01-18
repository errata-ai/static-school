---
title: Jekyll
homepage: https://jekyllrb.com

description: A simple, blog-aware static site generator.

intro: |
    Jekyll is a "simple, blog-aware, static site generator perfect for personal,
    project, or organization sites." Its first release dates back to 2009,
    making it one of the most mature static site generators available. It has
    built-in support for [GitHub Pages](https://bit.ly/30cxGPN) and one of the
    largest collections of community-maintained
    [themes](https://jekyllrb.com/docs/themes/) available.

language:
  name: Ruby
  link: https://www.ruby-lang.org/en/
  icon: devicon-ruby-plain colored

templating:
  name: Liquid
  link: https://shopify.github.io/liquid/

license:
  name: MIT
  slug: mit

localization: false
versioning: false
theming: true

adoc: true
md: true
rst: false

twitter: jekyllrb
repo: jekyll/jekyll
---

## Markup

Jekyll has [native support][1] for the Kramdown flavor of Markdown (a non-standard implementation), and supports
[CommonMark][3] and [AsciiDoc][2] through third-party plugins (which were used in
the benchmarks below).

{{% chart-tabs %}}

[1]: https://jekyllrb.com/docs/configuration/markdown/#custom-markdown-processors
[2]: https://github.com/asciidoctor/jekyll-asciidoc
[3]: https://github.com/github/jekyll-commonmark-ghpages
