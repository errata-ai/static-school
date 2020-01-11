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

## Contributing

## Credits

This project was inspired by Netlify's MIT-licensed [StaticGen](https://www.staticgen.com/) website. The major difference is that *Static School* is much more than a "leaderboard": we provide in-depth benchmarking, guides, and tutorials.
