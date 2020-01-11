# Static School

Static Shool is an open-source project with the goal of making it easier to discover, research, and (ultimately) choose a static site generator (SSG) for your next project. We try to provide in-depth analysis for all SSGs we cover, including data (updated daily) on activity, popularity, and performance.

## Site Structure

Static School is built with [Hugo](https://gohugo.io/) and deployed daily with [Netlify](https://www.netlify.com/).

```text
├── LICENSE
├── README.md
├── bench <Files related to data collection and benchmarking>
├── config.toml
├── content
│   └── ssg/ <Individual pages for each SSG>
├── data
│   └── report.json <An auto-generated, JSON-formatted report of all our data>
├── layouts
├── resources
```

## Benchmarking

> **Dependecies**: To run the benchmark suite, you'll need [Python 3.7+](https://www.python.org/downloads/), [Pipenv](https://pipenv.kennethreitz.org/en/latest/), and [Docker](https://www.docker.com/products/docker-desktop) installed. 

Each static site generator is tested against three size increments 10, 100, and 1,000 files. The files are copied from a [corpus](https://github.com/errata-ai/static-school/tree/master/bench/corpus) of approximately-equivalent files for AsciiDoc, Markdown, and reStructuredText.

The following commands will build and run the benchmark suite:

```shell
$ cd bench
$ pipenv shell
$ make build
$ make bench ssg=<NAME OF SSG TO TEST>
```

The actual benchmarking is handled by the [hyperfine](https://github.com/sharkdp/hyperfine) command-line tool, which handles warmup runs, statistical outlier detection, and results formatting.

## Contributing

## Credits

This project was inspired by Netlify's MIT-licensed [StaticGen](https://www.staticgen.com/) website. The major difference is that *Static School* is much more than a "leaderboard": we provide in-depth benchmarking, guides, and tutorials.
