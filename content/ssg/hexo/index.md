---
title: Hexo
homepage: https://hexo.io/

description: A fast, simple & powerful blog framework.

intro: |
    Hexo is a "fast, simple, and powerful blog framework." It's designed to be
    extensible, including APIs for incorporating third-party template engines
    as wel as NPM packages (Babel, PostCSS, Less/Sass, etc).

language:
  name: JavaScript
  link: https://nodejs.org/en/
  icon: devicon-javascript-plain colored

templating:
  name: Swig
  link: https://github.com/node-swig/swig-templates

localization: true
versioning: false
theming: true

license:
  name: MIT
  slug: mit

adoc: false
md: true
rst: false

twitter: hexojs
repo: hexojs/hexo
---

## Markup

{{% callout class="info" %}}
**Note**: Hexo *does* have third-party plugins for AsciiDoc and
reStructuredText, but neither appear to be maintained&mdash;so they've been
omitted from this analysis.
{{% /callout %}}

Hexo supports Markdown through an [officially-maintained plugin][1] for
`markdown-it`, a CommonMark-compliant parser.

{{% chart-formats id="benchmark-ssgs" md="true" adoc="false" rst="false" %}}

Compared to other SSGs, Hexo's performance is pretty average across the board
with Jekyll being its most similar counterpart.

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

[1]: https://github.com/hexojs/hexo-renderer-markdown-it