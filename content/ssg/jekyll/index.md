---
title: Jekyll
homepage: "https://jekyllrb.com"

description: "A simple, blog-aware static site generator."
intro: >
    Jekyll is a simple, blog-aware, static site generator perfect for personal, project, or organization sites. Think of it like a file-based CMS, without all the complexity.

language:
  name: Ruby
  link: https://www.ruby-lang.org/en/

templating:
  name: Liquid
  link: https://shopify.github.io/liquid/

localization: false
versioning: false
theming: true

license: MIT

adoc: true
md: true
rst: false

twitter: jekyllrb

css: ["vendor/highslide.min.css"]

js: [
    "vendor/highcharts/highcharts.min.js",
    "vendor/highcharts/highcharts-more.min.js",
    "vendor/highcharts/data.min.js",

    "features/bench.js"
  ]
---

## Markup

{{% callout class="info" %}}
**Note**: *There is* a [plugin](https://github.com/xdissent/jekyll-rst) available for reStructuredText, but it hasn't been updated in **\~6 years**&mdash;so it was been omitted from this analysis.
{{% /callout %}}

Jekyll has [native support][1] for the Kramdown flavor of Markdown, and supports
[CommonMark][3] and [AsciiDoc][2] through third-party plugins (which are used in
the benchmarks below).

{{% chart id="benchmark-formats" %}}

As shown above, Jekyll's performance is relatively consistent between sites
using CommonMark and AsciiDoc: CommonMark was faster at every size increment,
but the most extreme difference (1,000 files) was only about 7 seconds.

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

## Conclusion

Coming soon.

[1]: https://jekyllrb.com/docs/configuration/markdown/#custom-markdown-processors
[2]: https://github.com/asciidoctor/jekyll-asciidoc
[3]: https://github.com/github/jekyll-commonmark-ghpages
