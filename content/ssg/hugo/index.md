---
title: Hugo
homepage: https://gohugo.io/

description: The world’s fastest framework for building websites.
intro: >
    Hugo is a static HTML and CSS website generator written in Go. It is optimized for speed, ease of use, and configurability.

language:
  name: Go
  link: https://golang.org/

templating:
  name: Go
  link: https://gohugo.io/templates/introduction/

localization: true
versioning: false
theming: true

license: Apache 2.0

adoc: true
md: true
rst: true

twitter: GoHugoIO

css: ["vendor/highslide.min.css"]

js: [
    "vendor/highcharts/highcharts.min.js",
    "vendor/highcharts/highcharts-more.min.js",
    "vendor/highcharts/data.min.js",

    "features/bench.js"
  ]
---

## Markup

{{% callout class="primary-2" %}}
**Key Takeaway**: If you're using AsciiDoc or reStructuredText, Hugo probably isn't a good choice.

Related discussion:

- [Asciidoc + Hugo performance](https://discourse.gohugo.io/t/asciidoc-hugo-performance/10637)
- [Shimgo Hugo](https://tychoish.com/post/shimgo-hugo/) (an attempt at improving reStructuredText + Hugo performance)
{{% /callout %}}

Hugo has native support for CommonMark, and supports AsciiDoc and reStructuredText through [external libraries][1]. While relying on plugins or external libraries isn't unusual, it has a dramatic impact on Hugo's performance:

{{% chart id="benchmark-formats" %}}

As you can, see the overhead of calling out to external libraries all but eliminates Hugo's claim to being "the world’s fastest": At a size of 1,000 files, AsciiDoc is **about 35.8 times slower** and reStructuredText is **about 70.6 times slower** than CommonMark.

[1]: https://gohugo.io/content-management/formats/#list-of-content-formats
