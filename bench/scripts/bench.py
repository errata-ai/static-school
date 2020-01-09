import json
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
        subprocess.check_output(["cp", "-r", "example_site", ext]).decode("utf-8")

        # Populate with benchmark data:
        benchmark = (data / ("test." + ext)).read_text()
        for i in range(size):
            name = "{0}.{1}".format(meta["filename"].format(i), ext)
            with open(os.path.join(ext, path, name), "w+") as f:
                layout = meta["layout"]
                if type(layout) != str:
                    layout = meta["layout"][ext]

                f.write(layout.format(
                    title=meta["filename"].format(i),
                    content=benchmark
                ))

    args = [
        "hyperfine",
        "--export-json",
        "bench.json",
        "--style",
        "none",
        "--max-runs",
        "3"
    ]

    for ext in meta["formats"]:
        args.append(meta["commands"]["build"].format(dir=ext))

    subprocess.check_output(args)
    benchmark = subprocess.check_output(["cat", "bench.json"])

    version = subprocess.check_output(meta["commands"]["version"].split())

    result = json.loads(benchmark)
    result["version"] = version.decode("utf-8").split("\n")[0]

    print(json.dumps(result))
