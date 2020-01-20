---
title: Feature Matrix

layout: table
partial: feature-matrix

needsFa: true
css: [
    "https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css",
    "https://cdn.datatables.net/buttons/1.6.1/css/buttons.dataTables.min.css"
]
js: [
    "https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js",
    "https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js",
    "https://cdn.datatables.net/buttons/1.6.1/js/dataTables.buttons.min.js",
    "https://cdn.datatables.net/buttons/1.6.1/js/buttons.colVis.min.js",

    "/js/features/matrix.js"
]
---

{{% callout class="info" %}}
**Are we missing a feature?** Feel free to [submit a PR](https://github.com/errata-ai/static-school/pulls) that adds a new feature or updates a generator's entry for an existing feature.
{{% /callout %}}

The following table attempts to provide an objective comparison of static
site generators by *implementation-agnostic* features. In other words, we want
to focus on features *could* be implemented for any generator rather than
features that are tied to a certain tech stack (such as "available
as a single binary" or "has a rich component ecosystem").

Orange cells indicate that a certain feature is implemented through a
*third-party* plugin. Officially-maintained plugins are considered to be a
native feature (green cells).
