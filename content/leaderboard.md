---
title: Leaderboard
layout: leaderboard
---

The following table ranks static site generators by the time it takes them to build a 1,000-file site. The time shown for each static site generator is the mean of 3 separate builds (following 1 "warm up" build).

The times were recorded using the [`hyperfine`][1] command-line tool on a [Alpine-based Docker image][2] built specifically for each static site generator. While the use of Docker is somewhat unusual for benchmarking purposes, it makes it much easier to reproduce the results locally (or on a provisioned server) since each static site generator requires its own specific environment (runtime, plugins, etc).

[1]: https://github.com/sharkdp/hyperfine
[2]: https://github.com/errata-ai/static-school/tree/master/bench/generators
