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

features:
  localization:
    type: plugin
    link: https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites
  versioning: false
  custom_output: false
  asset_pipelines:
    type: plugin
    link: https://github.com/getpelican/pelican-plugins/tree/master/assets
  data_files: false
  image_processing:
    type: plugin
    link: https://github.com/whiskyechobravo/image_process
  extensible:
    link: https://docs.getpelican.com/en/stable/plugins.html

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

{{% chart-tabs %}}

[1]: https://github.com/Python-Markdown
[2]: https://github.com/Python-Markdown/markdown/issues/338
[3]: https://github.com/getpelican/pelican-plugins/tree/master/asciidoc_reader
