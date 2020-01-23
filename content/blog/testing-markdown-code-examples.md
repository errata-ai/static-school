---
title: Testing Markdown code examples
summary: Set up an automated test suite for your Markdown code blocks.

author: Joseph Kato
avatar: jdkato
category: markup

date: 2020-01-22T11:32:13-08:00

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

Testing code examples is an important aspect of maintaining user-friendly
documentation&mdash;I'm sure we can all relate to the frustration of attempting
to follow a tutorial only to find that the example code snippets no longer work
as intended.

In this post, we're going set up a testing framework that will help us ensure
that this doesn't happen to our own documentation. More specifically, our goals
are as follows:

- **Set up a language-agnostic testing framework**. Markdown can
  contain code examples of *any* language (Python, C++, JavaScript, etc.), but
  most existing solutions&mdash;such as [`markdown-doctest`][3] (JavaScript) or
  [`rustdoc`][4] (Rust)&mdash;focus on supporting a single language.

- **Leverage existing testing libraries**. Most programming
  languages have robust testing libraries already available and we don't want
  to "reinvent the wheel" or limit our testers to using a particular one.

- **Use [standards-compliant][5] Markdown**. Whenever you start
  talking about "enhancing" the abilities of Markdown, you can quickly find
  yourself moving *away* from actually writing Markdown: there are countless
  "flavors" and "implementations" that add features at the cost of
  standardization.

## Getting Started

In a [previous post][1], we discussed using the [Markdata library][2] to help
us maintain "data" (tables, code blocks, command-line output, etc.) in our
Markdown. Now, we're going to take it a step further and detail exactly how we
can use Markdata to set up an automated test suite for all of our embedded
code examples.

### Installation

Markdata is itself a Python (3.6.0+) library and so we'll need to first ensure
that Python is installed.

You can find the official download links on the [Python website][6]. To verify
that you're ready to proceed, enter the following command in your command
prompt or terminal:

```console
$ python3 --version
Python 3.7.4
```

If your version is greater than 3.6, you're all set. Next, we need to install
[Markdata][2] using `pip` ([Python's package manager][7]):

```console
$ pip3 install markdata
...
$ markdata --help
...
```

### Project Structure

While there are no directory structure requirements for using Markdata,
*you do* need to ensure that your code snippets aren't actually written in your Markdown itself. In other words, we'll write our code examples in their own
language-specific files (for example, `.py` for Python) and then include them
in our Markdown prior to building our documentation.

In practice, this will look something like the following example:

```text
.
├── code
│   ├── js
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   └── test.js
│   └── py
│       ├── requirements.txt
│       └── test.py
└── docs
    └── doc1.md
```

Here,  we'll have a Markdown file (`doc1.md`) that includes two fully-tested
code examples in two different languages: `js` (JavaScript) and `py` (Python),
which will both use their own language-specific testing framework.

- Our first example, Python, will use a real-world code example from the
[`ruamel.yaml`][8] documentation and the [pytest framework][9]:

  ```python
  """Testing Python with Markdata

  Usage: $ pytest test.py
  """


  def test_yaml():
      """An example of testing a Python code snippet.
      """
      # Snippet start
      from ruamel.yaml import YAML

      inp = """\
      - &CENTER {x: 1, y: 2}
      - &LEFT {x: 0, y: 2}
      - &BIG {r: 10}
      - &SMALL {r: 1}
      # Override
      - <<: [*BIG, *LEFT, *SMALL]
        x: 1
        label: center/big
      """

      yaml = YAML()
      data = yaml.load(inp)
      assert data[4]['y'] == 2
      # Snippet end
  ```

- Our second example, JavaScript, will use a code example from the
  [Mozilla developer docs][10] and the [mocha framework][11]:

  ```js
  /* test.js: Testing Node.js with Markdata

  Usage: ./node_modules/mocha/bin/mocha */
  var assert = require('assert');

  describe('Array', function() {
    describe('#indexOf()', function() {
      it('should report the correct index', function() {
          // Snippet start
          var array = [2, 9, 9];
          array.indexOf(2);     // 0
          array.indexOf(7);     // -1
          array.indexOf(9, 2);  // 2
          array.indexOf(2, -1); // -1
          array.indexOf(2, -3); // 0
          // Snippet end

          assert.equal(array.indexOf(2), 0);
          assert.equal(array.indexOf(7), -1);
          assert.equal(array.indexOf(9, 2), 2);
          assert.equal(array.indexOf(2, -1), -1);
          assert.equal(array.indexOf(2, -3), 0);
      });
    });
  });
  ```

Both files contain quite a bit of test-related "boilerplate" that we *don't*
want to show in our rendered documentation (our actual snippets are denoted by
the start/end comments). This illustrates one of the key features of
Markdata&mdash;it allows us to specify a line number range to extract
(which you'll see below).

Now, in our Markdown file we make use of [Markdata's built-in `code`][12]
directive:

```markdown
# Markdata Example (`doc1.md`)

Here's the Python code snippet from `ruamel.yaml `:

`code{'path': 'code/py/test.py', 'span': [11, 39], 'lang': 'python'}`

And here's our Mozilla code snippet:

`code{'path': 'code/js/test.js', 'span': [9, 14], 'lang': 'js'}`
```

As you can see, this is a 100% standards-compliant Markdown file: Markdata's
directives overload the existing containers for raw strings (in this case,
*code spans*). We are also able to specify the exact range of lines (the `span`
key) that we want to display in our rendered documentation.

Finally, we can call the `markdata` executable to compile our Markdown
document:

```console
$ markdata doc1.md
```

~~~markdown
# Markdata Example (`doc1.md`)

Here's the Python code snippet from `ruamel.yaml `:

```python
from ruamel.yaml import YAML

inp = """\
- &CENTER {x: 1, y: 2}
- &LEFT {x: 0, y: 2}
- &BIG {r: 10}
- &SMALL {r: 1}
# Override
- <<: [*BIG, *LEFT, *SMALL]
  x: 1
  label: center/big
"""

yaml = YAML()
data = yaml.load(inp)
assert data[4]['y'] == 2
```

And here's our Mozilla code snippet:

```js
var array = [2, 9, 9];
array.indexOf(2);     // 0
array.indexOf(7);     // -1
array.indexOf(9, 2);  // 2
array.indexOf(2, -1); // -1
array.indexOf(2, -3); // 0
```
~~~

And that’s it. We now have a Markdown document containing our
desired, well-formatted code examples extracted from their designated test
files.

### Continuous Integration & Delivery

The final step is to incorporate this process into a more realistic build
system. For example purposes, we're using [Travis CI][13] and [Hugo][14]:

```yaml
script:
  # Step 1: Run the Python tests.
  - cd code/py
  - pip install -r requirements.txt
  - pytest test.py
  - cd -

  # Step 2: Run the Node.js tests.
  - cd code/js
  - npm install
  - ./node_modules/mocha/bin/mocha
  - cd -

after_success:
  # Step 3: Compile our Markdown.
  - markdata --root . docs content/post

  # Step 4: Build our site.
  - hugo
```

Most of these steps will depend on the particular languages and tech you're
using, but "Step 3" is an important detail: we're converting all *Markdata* files
in the `docs` directory into *Markdown* files stored in `content/post` (Hugo's
default content directory). This is something that you'll want to do regardless
of what static site generator you're using, as it allows the generator to
publish HTML containing the actual code examples.

[1]: /blog/fixing-markdowns-shortcomings-with-python/
[2]: https://pypi.org/project/markdata/
[3]: https://github.com/Widdershin/markdown-doctest
[4]: https://doc.rust-lang.org/rust-by-example/meta/doc.html
[5]: https://commonmark.org/
[6]: https://www.python.org/downloads/
[7]: https://packaging.python.org/tutorials/installing-packages/
[8]: https://yaml.readthedocs.io/en/latest/example.html
[9]: https://docs.pytest.org/en/latest/index.html
[10]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf#Examples
[11]: https://mochajs.org/
[12]: https://github.com/errata-ai/markdata#directives
[13]: https://travis-ci.org/
[14]: https://gohugo.io/
