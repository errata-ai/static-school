import os
import pathlib
import subprocess
import sys

import yaml


def parse_meta():
    """Parse and return the SSG's meta data.
    """
    with open("meta.yml") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == "__main__":
    size = int(sys.argv[1])
    data = pathlib.Path("corpus")

    meta = parse_meta()
    path = meta["content"]

    for ext in meta["formats"]:
        # Create a site for each format:
        subprocess.check_output(
            meta["commands"]["new"].format(dir=ext),
            shell=True
        ).decode("utf-8")

        # Populate with benchmark data:
        benchmark = (data / ("test." + ext)).read_text()
        for i in range(size):
            name = "test{0}.{1}".format(i, ext)
            with open(os.path.join(ext, path, name), "w+") as f:
                f.write(meta["layout"].format(content=benchmark))

    args = [
        "hyperfine",
        "--export-json",
        "bench.json",
        "--style",
        "none",
        "--warmup",
        "3",
        "--max-runs",
        "5"
    ]

    for ext in meta["formats"]:
        args.append(meta["commands"]["build"].format(dir=ext))

    subprocess.check_output(args)

    benchmark = subprocess.check_output(["cat", "bench.json"])
    print(benchmark.decode("utf-8"))