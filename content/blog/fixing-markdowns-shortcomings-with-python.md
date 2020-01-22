---
title: Fixing Markdown’s shortcomings with Python
summary: A new take on using Markdown for technical documentation.

author: Joseph Kato
avatar: jdkato
category: markup

date: 2019-02-18T11:40:57-08:00

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

[Markdown][1] has become the go-to lightweight markup language for a variety of tasks — you’ll find it powering commenting systems, blogs, wikis, and static websites of all sorts. This widespread adoption has led to a number of advantages over other markup languages — namely, AsciiDoc and reStructuredText — when it comes to writing technical documentation:

{{% callout class="info" %}}
**Note**: When I refer to "AsciiDoc," I’m talking about the variation of the syntax compatible with the Asciidoctor toolchain (not the older Python implementation).
{{% /callout %}}

- **Familiarity**. Almost everyone in the technical writing community (developers, writers, editors, etc.) has some experience with Markdown. And while AsciiDoc and reStructuredText (to a lesser extent) are becoming more popular, they’re still foreign to many people.

- **Tooling**. Markdown has a larger and more mature selection of tooling available — including linters ([which AsciiDoc currently lacks altogether][2]), standalone editors, and static site generators.

- **Performance**. Markdown has a *native* implementation in [many languages][3], while AsciiDoc (Ruby, JavaScript, and Java) and reStructuredText (Python) have fairly limited support. This can lead to performance issues, as is the case with [AsciiDoc/reStructuredText and Hugo](/ssg/hugo).

One of the reasons that Markdown is so popular is its simple, easy-to-read syntax ([that can be learned in as little as 10 minutes][4]). Unfortunately, the simplicity of Markdown also means that it’s missing some important features that are available (to some extent) in both AsciiDoc and reStructuredText:

- **Support for content reuse**. Perhaps the most important of Markdown’s missing features is the ability to include content from other files.

- **Management of tabular data**. While this isn’t technically a "missing" feature, Markdown is notoriously bad at handling tables: they’re a pain to write, hard to maintain, and you’re limited to the most basic of layouts.

- **Extensibility**. The inability to extend Markdown’s syntax often forces us to write HTML for fairly simple tasks such as applying classes to elements or embedding multimedia.

The most common solution to the above issues is to either use a more feature-rich flavor of Markdown (e.g., [Python-Markdown][5]) or a template language (e.g., [Liquid][6]). There are, however, a few drawbacks to doing so:

- Depending on features that are tied to a particular flavor or static site generator (as is the case with many template languages), means that you’re effectively eliminating Markdown’s advantage in tooling: What good is having a wide selection of static site generators if switching between them requires significant reformatting? What good are linters if you have to use syntax that they don’t understand?

- By deviating from Markdown’s "standard" syntax (i.e., the [CommonMark Spec][1]), you’re sacrificing Markdown’s simplicity and, by extension, its advantage in familiarity.

Another solution is to give up Markdown altogether: the sentiment that its flaws make it an inadequate choice for technical documentation is becoming increasingly popular. The problem here, aside from ignoring the strengths of Markdown, is that many of us aren’t in a position to make such a change. Any combination of lacking time, approval, or desire can make such a suggestion a non-starter.

But what if there was an option that addressed Markdown’s weaknesses without sacrificing its strengths?

## Introducing "Markdata"

[Markdata][7] is an open-source, MIT-licensed Python library and command-line tool for managing "data" (essentially, any non-prose supplement that might appear in your markup — e.g., code, diagrams, tables, etc.) in Markdown files. There are a few driving principles behind this library:

- **Accept Markdown for what it is (and isn’t)**. Markdown, unlike many markup languages, is designed to be converted into a single format: (X)HTML. So, in order to get the most out of Markdown, you need to embrace the fact that you’ll need to know and use HTML — it’s currently the only portable way to extend Markdown’s syntax.

- **Avoid doing too much in your markup**. Conditional logic, looping constructs, HTML, source code, and tables should not be directly written in your markup.

- **Single-source whenever possible**. This is related to the previous point, but it’s worth re-stating: keeping your documentation DRY should be one of your highest priorities. All non-prose supplements — such as HTML snippets, code examples, and tabular data — should be written once and included elsewhere.

By adhering to the above principles, Markdata is able to extend Markdown in meaningful ways without deviating from CommonMark.

## Getting Started

Markdata is [available on PyPI][8] (Python >= 3.6.0):

```console
$ pip install markdata
...
$ markdata --help
...
```

Markdata’s functionality is driven by directives, which are Markdown snippets that call Python functions. Instead of introducing new syntax, directives overload the existing containers for raw strings: code spans and code blocks.

The basic idea is that you specify the name of a Python function and its expected arguments within your markup:

```markdown
### This is a Markdown file

Here's an inline (code span) directive:

`name_of_function{'arg1': 'value', 'arg2': 'value2'}`
```

And then you write the implementation in a separate Python source file:

```python
def main(meta, arg1, arg2):
    """An example directive.

    These functions return a string that replaces the original
    directive in the Markdown source file.

    `meta` is a dictionary created from front matter (`{}` by
    default). In this case, it will be:

        {'title': 'An example Markdown file'}
    """
    return 'this is a string'
```

You’ll typically store these directives in a directory close to your Markdown content and then tell `markdata` where to look:

```console
$ ls content
directives/  file1.md  file2.md
$ markdata --directives='content/directives' content
...
```

In other words, Markdata acts as more of a "preprocessor" than an actual implementation: you call the markdata executable prior to (not instead of) another Markdown library.

Now that you know the basics, let’s look at some real use cases.

### Content reuse

The `document` directive (one of Markdata’s built-in directives) brings content reuse to Markdown. To use this directive, you specify a path (relative to the directive-containing file) and, optionally, a span of lines:

```markdown
By including code examples from external sources, we can ensure that they're properly tested, linted, and updated without having to duplicate content.

`code{'path': 'my_file.py', 'span': [10, 13], 'lang': 'python'}`

We can include non-code content, too:

`document{'path': 'includes/some_file.md'}`
```

In the example above, we inserted lines 10 through 13 of my_file.py into a Python code block and included the entire contents of some_file.md at the end. To perform the insertions, simply call the markdata executable on the file:

```console
$ markdata my_file.md
...
```

### Tables

`table` is another built-in directive. It allows you to write, edit, and maintain your tables in YAML, JSON, or CSV files. For example, consider the following YAML sequence:

```yaml
---
-
  age: 90
  first_name: John
  last_name: Adams
-
  age: 83
  first_name: Henry
  last_name: Ford
```

To turn this into a table, we simply use the directive:

```markdown
`table{'path': 'data.yml', 'classes': ['table'], 'caption': 'My data'}`
```

After calling `markdata` executable, we get:

```html
<table class="table">
    <caption>My data</caption>
    <thead>
        <tr>
            <th>age</th>
            <th>first_name</th>
            <th>last_name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>90</td>
            <td>John</td>
            <td>Adams</td>
        </tr>
        <tr>
            <td>83</td>
            <td>Henry</td>
            <td>Ford</td>
        </tr>
    </tbody>
</table>
```

If the basic layout supported by table doesn’t fit your personal needs, you’re free to create [custom directives][9] that can produce any layout possible in HTML.

### Multimedia

What if we want to include a YouTube video or Instagram post in our Markdown? With Markdata, we simply write a directive!

To embed a YouTube video, for example, we could do something like this:

```python
def main(meta, video, clip=[]):
    """Example directive for including a YouTube video.

    `meta` is a dictionary containing any front matter that was
    listed in the Markdown file.

    `clip` specifies an optional start and stop point for the video.
    """
    link = "https://www.youtube.com/embed/{0}".format(video)

    if clip:
        link += "?start={0}&end={1}".format(*clip)

    return '<iframe src="{0}"></iframe>'.format(link)
```

And then, we can simply use the directive in our Markdown:

```markdown
`youtube{'video': 'rfscVS0vtbw', 'clip': [36, 65]}`
```

Of course, you could also add HTML classes and attributes to allow for more precise styling and positioning.

### Semantic meaning

Adding *meaning* to elements is another common use case for Markdata.

Let’s say that we want to be able to use [Bootstrap-style][10] alerts and add classes to our paragraphs. Once again, we write custom directives:

```python
import mistune

def main(meta, content, level):
    """A Bootstrap-style alert.
    """
    # We want to be able to write our body content in Markdown,
    # so we use the `mistune` library to convert it to HTML.
    html = mistune.markdown(content)
    return '<div class="alert alert-{0}" role="alert">{1}</div>'.format(level, html)
```

```python
import mistune

def main(meta, content, classes=[]):
    """Adding classes to a `<p>`.
    """
    html = mistune.markdown(content)
    return html.replace("<p>", '<p class="{0}">'.format(" ".join(classes)))
```

We can now use both of these as block-level directives:

```markdown
# This is a Markdown file

Let's use an alert:

(```)alert{'level': 'warning'}
Here's *some* Markdown content.
(```)

Now, let's make a paragraph:

(```)paragraph{'classes': ['my-class', 'another-class']}
Here's the **body** of the paragraph.
(```)
```

### Leveraging the power of Python

All of the examples so far have been pretty straightforward: we use Python as a middle ground between Markdown and HTML, allowing us to add features without straying from CommonMark syntax.

But, as you can probably imagine, the ability to write arbitrary Python means that we can do much more than text-based substitutions. Here are some ideas:

- Create tables by making calls to APIs or databases at build time.

- Use plots that update at build time using one of Python’s plotting libraries (e.g., Seaborn).

- Include output from command-line tools by directly executing them.

- Implement directives in another programming language that you call via Python (e.g., `execute{'runtime': 'node', 'path': 'script.js'}`).

- ... and more!

## Conclusion

Markdata takes a new approach to an old problem: it allows us to extend Markdown without breaking away from CommonMark. It also allows us to move most template-related logic out of our markup source, making our documentation easier to maintain and less dependent on specific template languages.

The downsides are that it requires familiarity with Python and an additional build step.

Markdata is still in early development and I’d love to hear any thoughts or suggestions. Feel free to open an issue at the [GitHub repository][7]!

[1]: https://commonmark.org/
[2]: https://github.com/asciidoctor/asciidoctor-extensions-lab/issues/6
[3]: https://github.com/commonmark/commonmark-spec/wiki/list-of-commonmark-implementations
[4]: https://commonmark.org/help/
[5]: https://github.com/Python-Markdown/markdown/wiki/third-party-extensions
[6]: https://shopify.github.io/liquid/
[7]: https://github.com/errata-ai/markdata
[8]: https://pypi.org/project/markdata/
[9]: https://github.com/errata-ai/markdata#writing-your-own
[10]: https://getbootstrap.com/docs/4.3/components/alerts/
