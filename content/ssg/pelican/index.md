---
title: Pelican
homepage: https://blog.getpelican.com/

description: Pelican is a static site generator that requires no database or server-side logic.

intro: |
    Pelican is a static site generator that "requires no database or
    server-side logic." It features a modular plugin system and an
    officially-maintained
    [plugin repository](https://github.com/getpelican/pelican-plugins).

language:
  name: Python
  link: https://www.python.org/
  icon: devicon-python-plain colored

templating:
  name: Jinja2
  link: https://jinja.palletsprojects.com/en/2.10.x/

license:
  name: AGPL-3.0
  slug: aglp-3

localization: true
versioning: false
theming: true

adoc: true
md: true
rst: true

twitter: getpelican
repo: getpelican/pelican
---

## Markup

Pelican has native support for [Python-Markdown][1] (a [non-standard][2] Markdown implementation) and reStructuredText. AsciiDoc is supported through a [third-party plugin][3].

{{% chart id="benchmark-formats" %}}

From a performance standard point, reStructuredText is best markup language for Pelican: it was consistently the fastest at every size, often being almost twice as fast as Markdown and AsciiDoc.

{{% chart-formats id="benchmark-ssgs" md="true" adoc="true" rst="true" %}}

While Pelican lags behind other generators at building Markdown and AsciiDoc, it's currently the fastest at building reStructuredText&mdash;recording a time more than twice as fast as Hugo.

[1]: https://github.com/Python-Markdown
[2]: https://github.com/Python-Markdown/markdown/issues/338
[3]: https://github.com/getpelican/pelican-plugins/tree/master/asciidoc_reader
