---
title: Gatsby
homepage: https://www.gatsbyjs.org/

description: Build blazing fast, modern apps and websites with React.

language:
  name: JavaScript
  link: https://nodejs.org/en/
  icon: devicon-javascript-plain colored

templating:
  name: React
  link: https://reactjs.org/

localization: true
versioning: false
theming: true

license:
  name: MIT
  slug: mit

adoc: true
md: true
rst: false

twitter: gatsbyjs
repo: gatsbyjs/gatsby
---

## Markup

{{% callout class="info" %}}
**Note**: Although Gatsby supports AsciiDoc, it hasn't yet been included in the benchmarking below.
{{% /callout %}}

Gatsby supports both [Markdown][1] and [AsciiDoc][2] through officially-maintained plugins (the Markdown plugin uses [remark][3], though, which is a [non-standard][4] processor).

Gatsby also includes support for [MDX][5], an "authorable format that lets you seamlessly write JSX in your Markdown documents."

{{% chart id="benchmark-formats" %}}

Despite Gatsby's claim of being "blazing fast," it finished last in our benchmarking of Markdown build speeds at every size:

{{% chart-formats id="benchmark-ssgs" md="true" adoc="false" rst="false" %}}

Of course, a static site generator can be "fast" in more ways than one and
Gatsby still offers a number of appealing features (which we'll discuss below).

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

[1]: https://www.gatsbyjs.org/packages/gatsby-transformer-remark/
[2]: https://www.gatsbyjs.org/packages/gatsby-transformer-asciidoc/
[3]: http://remark.js.org/
[4]: https://github.com/remarkjs/remark/issues/306
[5]: https://www.gatsbyjs.org/docs/mdx/
