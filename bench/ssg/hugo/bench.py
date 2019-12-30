import pathlib
import subprocess
import sys

HUGO = {
    "new": "hugo new site {dir}",
    "build": "hugo --config={dir}/config.toml --contentDir={dir}/content",
    "post": "hugo new post/test.{dir}"
}
DATA = pathlib.Path("corpus")
META = """
---
title: Benchmark
date: 2019-12-29T18:09:15-08:00
draft: false
---

{content}
"""

if __name__ == "__main__":
    size = int(sys.argv[1])
    for ext in ["md", "adoc", "rst"]:
        # Create a Hugo site for each format:
        subprocess.check_output(
            HUGO["new"].format(dir=ext).split()
        ).decode("utf-8")

        # Create a 'post' category for each format:
        subprocess.check_output(
            HUGO["post"].format(dir=ext).split(), cwd=ext
        ).decode("utf-8")

        # Populate the 'post' category with benchmark data:
        benchmark = (DATA / ("test." + ext)).read_text()
        for i in range(size):
            name = "test{0}.{1}".format(i, ext)
            with open("{0}/content/post/{1}".format(ext, name), "w+") as f:
                f.write(META.format(content=benchmark))

    print(subprocess.check_output([
        "hyperfine",
        "--warmup",
        "3",
        "--max-runs",
        "5",
        HUGO["build"].format(dir="adoc"),
        HUGO["build"].format(dir="md"),
        HUGO["build"].format(dir="rst")
    ]).decode("utf-8"))
