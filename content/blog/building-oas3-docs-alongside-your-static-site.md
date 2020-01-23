---
title: Building OAS3 docs alongside your static site
summary: Learn how to build OpenAPI Specification files from Markdown.

author: Joseph Kato
avatar: jdkato
category: markup

date: 2019-09-24T11:40:57-08:00

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

This post outlines a method for creating [OpenAPI Specification][1] (OAS) files using a build technique similar to how static site generators (SSGs) build their sites. The goals are fairly simple:

- > **Goal**: We want to write our [CommonMark-formatted](https://swagger.io/docs/specification/basic-structure/#metadata), user-facing API documentation in actual Markdown files (not JSON or YAML).
  >
  > **Motivation**: If you've ever worked on large OAS-based API docs before, you're very likely to have encountered `description` [entries like this](https://idratherbewriting.com/learnapidoc/docs/rest_api_specifications/openapi_openweathermap.yml). This is a YAML file containing embedded Markdown, which in turn contains some embedded HTML. We'd like to avoid this for many of the same reasons that static websites aren't simply built from HTML: it's easier to write and maintain documentation in dedicated markup files.

- > **Goal**: We want to employ automated linting (spelling and style checks) of our content to ensure that we have mistake-free and on-brand documentation.
  >
  > **Motivation**: One of the common issues with typical OAS spec maintenance is the lack of quality assurance (QA) options. Since prose is often embedded in YAML or JSON, it can be difficult to spell check, lint, and format. We want to be able to use the same CI-based testing techniques we use on our static site content.

- > **Goal**: We want to automate the creation of our OAS spec from our linted content.
  >
  > **Motivation**: Since we're now viewing our OAS spec as a read-only output artifact, we need a way to automate its creation from our static API documentation.

- > **Goal**: We want to be able to deploy our rendered API docs with the output of any static site generator.
  >
  > **Motivation**: Since we're now developing our API docs using the same toolchain and workflow as our static site, we want to be able to deploy them in the same way and at the same time using tools like [Swagger UI](https://swagger.io/tools/swagger-ui/).

Essentially, we're replacing the typical SSG workflow of `markup -> HTML` with `markup -> OAS -> HTML`. While this may seem unusual to some (especially those that already generate their OAS spec from source code) the idea of writing an API's spec "first" (i.e., by hand rather than from existing source code) isn't new: the concept is commonly referred to as ["spec-first development"][2] and has become increasingly popular. We're simply making the process easier to integrate with static site generators and markup-related tooling.

# File Structure

As with any SSG, the key to this workflow is using a consistent and standardized file structure. The exact details will depend on which SSG you'd like to integrate your API docs with, but we'll be using [Docusaurus][3] for the purposes of this document.

The [basic structure of a Docusaurus site][4] is given below:

```text
├── Dockerfile
├── docker-compose.yml
├── docs
│   ├── doc1.md
│   ...
└── website
    ├── README.md
    ├── blog
    │   ├── 2016-03-11-blog-post.md
    │   ...
    ├── core
    │   └── Footer.js
    ├── package.json
    ├── pages
    │   └── en
    │       ├── help.js
    │       ├── index.js
    │       └── users.js
    ├── sidebars.json
    ├── siteConfig.js
    ├── static
    │   ├── css
    │   │   └── custom.css
    │   └── img
    │       ├── docusaurus.svg
    │       ├── favicon
    │       │   └── favicon.ico
    │       ├── favicon.png
    │       └── oss_logo.png
    └── yarn.lock
```

In the [ `static` directory][5], we create an `api` sub-directory that contains Swagger UI's [`dist` contents][6]:

```text
website/static/api
├── img
│   ├── favicon-16x16.png
│   └── favicon-32x32.png
├── index.html
├── js
│   ├── swagger-ui-bundle.js
│   ├── swagger-ui-standalone-preset.js
│   ...
├── oauth2-redirect.html
├── spec.yml [added to .gitignore]
├── src
│   ...
└── template.yml
```

## `index.html` and `spec.yml`

The first two files we need to discuss are `index.html` and `spec.yml`. The [`index.html`](https://github.com/errata-ai/vale-server/blob/master/website/static/api/index.html) file is pretty standard, except for its reference to `spec.yml`:

```html
<script>
window.onload = function() {
  // Begin Swagger UI call region
  const ui = SwaggerUIBundle({
    url: "spec.yml", // ADD THIS
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })
  // End Swagger UI call region
  window.ui = ui
}
</script>
```

For our purposes, the `spec.yml` file is a read-only build artifact (see Build Process below) and should be added to your `.gitignore` file (or equivalent).

## `template.yml`

`template.yml` should contain all non-generated sections of your specification:

```yaml
openapi: 3.0.2

servers:
  - url: http://127.0.0.1:7777

tags:
  - name: Linting and Suggestions
    description: Find errors and receive possible solutions
  - name: Local Resources
    description: Get information about the active project and local Vale resources

externalDocs:
  description: Vale Server user documentation
  url: https://errata-ai.github.io/vale-server/docs/about

components:
  schemas:
    Suggestions:
      type: array
      items:
        type:
          string
    Action:
      type: object
      required:
        - Name
        - Params
      properties:
        Name:
          type: string
        Params:
          type: array
          items:
            type: string
    Alert:
      type: object
      required:
        - Action
        - Check
        - Description
        - Line
        - Link
        - Message
        - Severity
        - Span
        - Match
      properties:
        Action:
          $ref: "#/components/schemas/Action"
        Check:
          type: string
        Description:
          type: string
        Line:
          type: integer
        Link:
          type: string
        Message:
          type: string
        Severity:
          type: string
        Span:
          type: array
          items:
            type: string
        Match:
          type: string
    Alerts:
      type: array
      items:
        $ref: "#/components/schemas/Alert"
```

As you can see, it's a *very* abbreviated version of a typical spec that mostly consists of non-prose content that doesn't change often.

## The `src/` Directory

The `src/` directory is where most of our writing will take place. It includes our [`info`](https://swagger.io/specification/#infoObject) section (`info.md`), [`parameters`](https://swagger.io/specification/#parameterObject) (`parameters/`), and [`paths`](https://swagger.io/specification/#pathsObject) (`endpoints/`):

```text
website/static/api/src
├── endpoints
│   ├── path
│   │   └── get.md
│   ├── suggest
│   │   └── post.md
│   └── vale
│       └── post.md
├── info.md
└── parameters
    ├── alert.md
    ├── format.md
    └── text.md
```

From here, the process should be similar to how most SSGs generate their content: we write in Markdown files that use YAML-formatted front matter for metadata.

### `info.md`

Here's what our `info` section would look in YAML:

```yaml
info:
  title: Vale Server API
  version: 1.0.0
  contact:
    email: support@errata.ai
  description: |-
    The Vale Server API provides a means of communicating with the Vale Server desktop application, which manages user settings and interfaces with the Vale CLI tool, from third-party "client" applications:

    <img src="/vale-server/img/flow.svg" alt="An illustration of Vale Server's API flow." style="margin: auto; min-width: 50%; display: block;">

    All of the official Vale Server clients&mdash;[Atom][1], [Sublime Text][2], [Visual Studio Code][3], [Google Docs][5], and [Google Chrome][4]&mdash;use this API to communicate with the core desktop application.

    **NOTE**: Unlike most production APIs, the Vale Server API is embedded within the desktop application itself and runs on `localhost`. This means that users don't have to send their text to a remote server, but it also means that **you'll have to have an instance of Vale Server running to test the API here**.

    [1]: https://github.com/errata-ai/vale-atom
    [2]: https://github.com/errata-ai/SubVale
    [3]: https://github.com/errata-ai/vale-vscode
    [4]: https://errata-ai.github.io/vale-server/docs/chrome
    [5]: https://errata-ai.github.io/vale-server/docs/gdocs
```

However, instead of trying to edit and maintain this embedded Markdown in our spec itself, we write the description in `/api/src/info.md`:

```markdown
---
title: Vale Server API
version: 1.0.0
contact:
  email: support@errata.ai
---

The Vale Server API provides a means of communicating with the Vale Server desktop application, which manages user settings and interfaces with the Vale CLI tool, from third-party "client" applications:

<img src="/vale-server/img/flow.svg" alt="An illustration of Vale Server's API flow." style="margin: auto; min-width: 50%; display: block;">

All of the official Vale Server clients&mdash;[Atom][1], [Sublime Text][2], [Visual Studio Code][3], [Google Docs][5], and [Google Chrome][4]&mdash;use this API to communicate with the core desktop application.

**NOTE**: Unlike most production APIs, the Vale Server API is embedded within the desktop application itself and runs on `localhost`. This means that users don't have to send their text to a remote server, but it also means that **you'll have to have an instance of Vale Server running to test the API here**.

[1]: https://github.com/errata-ai/vale-atom
[2]: https://github.com/errata-ai/SubVale
[3]: https://github.com/errata-ai/vale-vscode
[4]: https://errata-ai.github.io/vale-server/docs/chrome
[5]: https://errata-ai.github.io/vale-server/docs/gdocs
```

This file is much easier to write, update, and lint using our typical writing environment.

### `parameters/`

The next step is documenting our `parameters`. These are often shared between multiple endpoints using references, so we want to define them in their own files. Here's an example ([`api/src/parameters/format.md`](https://github.com/errata-ai/vale-server/blob/master/website/static/api/src/parameters/format.md)):

~~~markdown
---
name: format
in: formData
schema:
  type: string
---

The would-be file extension of `text`. In other words, since `text` is passed as a buffer (and not a file path), `format` informs Vale Server of how it should parse the provided content.

This value should include any leading "." characters, as is common practice with extension-extraction utilities such as [`path.extname(path)`](https://nodejs.org/api/path.html#path_path_extname_path) for Node.js:

​```js
path.extname('index.coffee.md');
// Returns: '.md'
//
// This is the expected value for `format`.
​```
~~~

The auto-generated YAML then becomes:

~~~yaml
format:
  name: format
  in: formData
  schema:
    type: string
  description: |-
    The would-be file extension of `text`. In other words, since `text` is passed as a buffer (and not a file path), `format` informs Vale Server of how it should parse the provided content.

    This value should include any leading "." characters, as is common practice with extension-extraction utilities such as [`path.extname(path)`](https://nodejs.org/api/path.html#path_path_extname_path) for Node.js:

    ```js
    path.extname('index.coffee.md');
    // Returns: '.md'
    //
    // This is the expected value for `format`.
    ```
~~~

### `endpoints/`

The final step is documenting our endpoints. The path structure for these are `api/src/endpoints/<NAME>/<METHOD>`&mdash;e.g., [`api/src/endpoints/suggest/post.md`](https://github.com/errata-ai/vale-server/blob/master/website/static/api/src/endpoints/suggest/post.md):

```markdown
---
summary: Retrieve suggestions to fix a given Alert

parameters:
  - $ref: '#/components/parameters/alert'

tags:
  - Linting and Suggestions

produces:
  - application/json

responses:
  200:
    description: An array of suggestions
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Suggestions'
  400:
    description: Missing parameter
    content:
      application/json:
        schema:
          type: object
          required:
            - error
          properties:
            error:
              type: string
              enum:
                - "missing 'alert'"

operationId: FindSuggestions
---

The `/suggest` endpoint accepts a `/vale`-generated Alert and returns an array of possible fixes for the error, warning, or suggestion. The array will be empty if no fixes are found.

Also, while the response of `/vale` depends on the user's configuration, the response of `/suggest` is deterministic: the same suggestions will *always* be returned for a particular Alert.
```

The generated YAML then becomes:

```yaml
/suggest:
    post:
      summary: Retrieve suggestions to fix a given Alert
      parameters:
      - $ref: '#/components/parameters/alert'
      tags:
      - Linting and Suggestions
      produces:
      - application/json
      responses:
        200:
          description: An array of suggestions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Suggestions'
        400:
          description: Missing parameter
          content:
            application/json:
              schema:
                type: object
                required:
                - error
                properties:
                  error:
                    type: string
                    enum:
                    - missing 'alert'
      operationId: FindSuggestions
      description: |-
        The `/suggest` endpoint accepts a `/vale`-generated Alert and returns an array of possible fixes for the error, warning, or suggestion. The array will be empty if no fixes are found.

        Also, while the response of `/vale` depends on the user's configuration, the response of `/suggest` is deterministic: the same suggestions will *always* be returned for a particular Alert.
```

# Build Process

To tie this altogether, we use a [Python script](https://github.com/errata-ai/vale-server/blob/master/ci/scripts/api.py) to generate our final OAS3-compliant specification. We can then easily incorporate our API docs into an existing CI test suite, such as the [`.travis.yml`](https://github.com/errata-ai/vale-server/blob/master/.travis.yml) example given below:

```yaml
script:
  # Lint our product and API docs using Vale:
  - ./bin/vale docs website/static/api/src
after_success:
  # Generate our OAS3 spec:
  - python3 ci/scripts/api.py
  # Publish our docs
  ...
```

This will lint both our product *and* API docs using [Vale](https://github.com/errata-ai/vale), and then publish all of our docs together. You can find the entire repository source and published results at [`errata-ai/vale-server`](https://github.com/errata-ai/vale-server/tree/master/website/static/api) and [`https://errata-ai.github.io/vale-server/api/index`](https://errata-ai.github.io/vale-server/api/index), respectively.


[1]: https://swagger.io/docs/specification/about/
[2]: https://www.google.com/search?q=spec+first+development
[3]: https://docusaurus.io/
[4]: https://docusaurus.io/docs/en/tutorial-create-new-site
[5]: https://docusaurus.io/docs/en/custom-pages
[6]: https://github.com/swagger-api/swagger-ui/tree/master/dist
