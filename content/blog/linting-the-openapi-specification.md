---
title: Linting the OpenAPI Specification
summary: A tutorial on linting your OpenAPI Specification files.

author: Joseph Kato
avatar: jdkato
category: linting

date: 2019-09-25T11:40:57-08:00

needsSyntax: true
css: [
    "//cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.18.0/build/styles/github-gist.min.css"
]
js: [
    "//cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.18.0/build/highlight.min.js",

    "/js/features/init-table.js",
    "/js/features/init-syntax.js"
]
---

# Introduction

[OpenAPI Specification][1] files provide machine-readable (JSON or YAML)
descriptions of APIs and often contain snippets of text suitable for linting.

The problem is that the target text can be hard to reach from a linting
perspective. For instance, consider the following basic example:

```yaml
openapi: 3.0.0
info:
  title: Sample API
  description: >-
    Optional multiline or single-line description in
    [CommonMark](http://commonmark.org/help/) or HTML.
  version: 0.1.9
servers:
  - url: http://api.example.com/v1
    description: >-
        Optional server description, e.g. Main (production) server
  - url: http://staging-api.example.com
    description: >-
        Optional server description, e.g. Internal staging server for testing
paths:
  /users:
    get:
      summary: Returns a list of users.
      description: >-
        Optional extended description in CommonMark or HTML.
      responses:
        '200':    # status code
          description: A JSON array of user names
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string
```

As you can see above, the only parts we're really interested in are the
`title`, `description` (which can contain Markdown), and `summary` keys.

In the following sections, we'll discuss the three main techniques for linting
specification files using [Vale][2] (an open-source linter for prose). For the
examples, we'll be referencing the [`petstore.yaml`][3] file from Swagger.

## Option 1: No Processing

| Pros                                                            | Cons                                                             |
|-----------------------------------------------------------------|------------------------------------------------------------------|
| Straightforward; no scripting or workflow adjustments required. | No support for syntax-related features.                          |
|                                                                 | More likely to encounter false positives related to formatting.  |
|                                                                 | Involves maintaining prose in JSON/YAML.                         |

The easiest way to lint an OpenAPI specification file is to simply pass it,
as is, to Vale:

```console
$ vale petstore.yaml
```

Vale will treat the file as plain text and lint its content line by line, but
you'll likely receive a lot of meaningless errors related to the formatting
syntax (JSON or YAML) and Vale won't be able to correctly parse any embedded
Markdown.

## Option 2: Post-Processing

| Pros                                 | Cons                                                     |
|--------------------------------------|----------------------------------------------------------|
| Full-featured, syntax-aware linting. | Scripting knowledge required.                            |
|                                      | Involves maintaining prose in JSON/YAML.                 |
|                                      | Linting output doesn't report meaningful file locations. |

The next option involves transforming your specification files after they've
already been created.

This will (generally speaking) probably feel like the most "natural" solution
as its methodology is quite similar to that of existing tools - for example,
[Swagger UI][4] (transforms specs for presentation) and [Swagger Codegen][5]
(transforms specs for consumption), etc.

### Option 2a: Key Extraction

The most obvious solution is to extract and lint the desired keys individually.
Thanks to the machine-readable nature of the specification files, this can be
done in a few lines of your favorite scripting language (such as Python,
which we're using below):

```python
import subprocess
import sys

# pip install PyYAML
import yaml


def lint_keys(data, keys):
    """Recursively lint the given data.
    """
    for k, v in data.items():
        if isinstance(v, dict):
            lint_keys(v, keys)
        elif k in keys:
            # NOTE: We use `--ext=.md` since the Petstore example
            # uses Markdown formatting in its descriptions.
            print(subprocess.check_output(["vale", "--ext=.md", "--no-exit", v]))


def lint(spec, sections, keys):
    """A lint a given OpenAPI specification file.
    """
    with open(spec, "r") as s:
        doc = yaml.load(s)
        for section in [s for s in doc if s in sections]:
            lint_keys(doc[section], keys)


if __name__ == "__main__":
    lint(
        sys.argv[1],
        # A list of spec sections to lint:
        sections=["info", "paths"],
        # A list of the keys we want to lint:
        keys=["description", "summary"],
    )
```

You can use this script by passing your spec as a parameter:

```console
$ python swagger.py petstore.yaml
...
```

### Option 2b (only OAS2): Swagger2Markup

Another option is to convert the entire specification into a format that Vale
can understand (AsciiDoc or Markdown) using the [Swagger2Markup][6] library.

For example, you'd use the following command to lint the Petstore example:

```console
$ java -jar swagger2markup-cli-1.3.3.jar convert -i petstore.yaml -f swagger && vale swagger.adoc
```

Unfortunately, since Vale is linting our content outside of the actual
specification file, both of these options don't report meaningful file
locations.

## Option 3: Pre-Processing

| Pros                                              | Cons                                   |
|---------------------------------------------------|----------------------------------------|
| Full-featured, syntax-aware linting.              | Scripting knowledge required.          |
| Avoids having to maintain prose in JSON/YAML.     | Access to source information required. |
| Linting output reports meaningful file locations. |                                        |

Up to this point, all of our options focus on working with a specification file
that already exists. This makes sense in a number of ways: it's similar to how
other OpenAPI tooling works, it makes no assumptions about where the
specification information comes from, and it can be integrated into almost any
existing workflow.

However, from a writing perspective, this workflow isn't ideal: if you're
interested in linting your specification files, then you're likely intending to
edit those files too (i.e., you'd surely fix any errors found). The problem
here is that the specification files themselves are a poor place to make
prose-related changes for a few reasons:

- It doesn't fix the source of the problem. Unless you're writing your
   specification files by hand (see option 3a below), fixing errors in the
   specification file itself doesn't actually fix the error in the content
   (usually a source code file) that the specification is based on.

- JSON and YAML files aren't good places for writing markup. If you write your
   endpoint descriptions in actual Markdown files, then you have full access to
   your typical writing environment: spell check, syntax highlighting, linter
   plugins, etc.

A better solution is to lint your content *prior* to generating the
specification file.

### Option 3a: Spec-First Development

If you write your specification files by hand (i.e., they aren't generated from
external source code files), then there's simply no reason to lint the
specification file itself: you should write your prose in individual Markdown
files, lint those files, and then generate your specification from the
already-linted content.

[You can find a Gist explaining how I implemented such a workflow here][8].

### Option 3b: Lint Your Source Code

If your specification is generated from external source code files, then you
should lint those files themselves. Vale has built-in support for linting
comments from many programming languages.

However, if your specification is derived from non-comment statements (such as
annotations), then you'll need to use a technique similar to Option 2a: parse
the source code (which replaces the JSON/YAML file), extract the annotations,
and pass them individually to Vale.

## Conclusion

There are many ways to use Vale to lint OpenAPI specification files, but
choosing the "best" solution likely depends on details that are specific to
your own workflow needs.

If you have any questions or run into any problems, feel free to open an issue
at the [Vale repository][7].

[1]: https://swagger.io/specification
[2]: https://github.com/errata-ai/vale
[3]: https://github.com/OAI/OpenAPI-Specification/blob/master/examples/v2.0/yaml/petstore.yaml
[4]: https://swagger.io/tools/swagger-ui/
[5]: https://swagger.io/tools/swagger-codegen/
[6]: https://github.com/Swagger2Markup/swagger2markup
[7]: https://github.com/errata-ai/vale/issues/new
[8]: https://gist.github.com/jdkato/156944741f134dca3d0a18dafcfa9803
