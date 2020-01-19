---
title: Hexo
homepage: https://hexo.io/

description: A fast, simple & powerful blog framework.

intro: |
    Hexo is a "fast, simple, and powerful blog framework." It's designed to be
    extensible, including APIs for incorporating third-party template engines
    and NPM packages (Babel, PostCSS, Less/Sass, etc).

language:
  name: JavaScript
  link: https://nodejs.org/en/
  icon: devicon-javascript-plain colored

templating:
  name: Swig
  link: https://github.com/node-swig/swig-templates

features:
  localization:
    link: https://hexo.io/docs/internationalization.html
  versioning: false
  custom_output: false
  asset_pipelines:
    type: plugin
    link: https://github.com/chenzhutian/hexo-all-minifier#readme
  data_files:
    link: https://hexo.io/docs/data-files
  image_processing:
    type: plugin
    link: https://github.com/ottobonn/hexo-image-sizes
  extensible:
    link: https://hexo.io/docs/plugins

localization: true
versioning: false
theming: true

license:
  name: MIT
  slug: mit

adoc: true
md: true
rst: false

twitter: hexojs
repo: hexojs/hexo
---

## Markup

Hexo supports Markdown through an [officially-maintained plugin][1] for
`markdown-it` (a CommonMark-compliant parser) and AsciiDoc through a [third-party plugin][2].

{{% chart-tabs %}}

[1]: https://github.com/hexojs/hexo-renderer-markdown-it
[2]: https://github.com/hcoona/hexo-renderer-asciidoc
