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

{{% callout class="info" %}}
**Key Takeaway**: Jekyll is a great choice if your using AsciiDoc to author your content: Both Jekyll and AsciiDoctor (AsciiDoc's toolchain) are written in Ruby, and Jekyll's AsciiDoc plugin is maintained by the core AsciiDoctor team.
{{% /callout %}}

Jekyll has [native support][1] for the Kramdown flavor of Markdown (a non-standard implementation), and supports
[CommonMark][3] and [AsciiDoc][2] through third-party plugins (which were used in
the benchmarks below).

{{% chart id="benchmark-formats" %}}

As shown above, Jekyll's performance is relatively consistent between sites
using Markdown and AsciiDoc: Markdown was faster at every size increment,
but the most extreme difference (1,000 files) was only about 7 seconds.

{{% chart-formats id="benchmark-ssgs" md="true" adoc="true" rst="false" %}}

Compared to other Markdown-based generators, Jekyll's performance is pretty average across the board. However, notably, Jekyll was consistently the **fastest** generator at building AsciiDoc in our test suite.

[1]: https://jekyllrb.com/docs/configuration/markdown/#custom-markdown-processors
[2]: https://github.com/asciidoctor/jekyll-asciidoc
[3]: https://github.com/github/jekyll-commonmark-ghpages
