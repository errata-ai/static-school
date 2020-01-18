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

localization: true
versioning: false
theming: true

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

{{% callout class="info" %}}
**Key Takeaway**: If you're using AsciiDoc or reStructuredText, Hugo probably isn't the best choice.

Related discussion:
- [Asciidoc + Hugo performance](https://discourse.gohugo.io/t/asciidoc-hugo-performance/10637)
- [Shimgo Hugo](https://tychoish.com/post/shimgo-hugo/) (an attempt at improving reStructuredText + Hugo performance)
{{% /callout %}}

Hugo has native support for Markdown (standards-compliant), and supports AsciiDoc and reStructuredText through [external libraries][1]. While relying on plugins or external libraries isn't unusual, it has a dramatic impact on Hugo's most popular selling point&mdash;performance:

{{% chart-tabs %}}

[1]: https://gohugo.io/content-management/formats/#list-of-content-formats
