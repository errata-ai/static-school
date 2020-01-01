import pathlib
import subprocess
import sys

import yaml


def parse_meta():
    """
    """
    with open("meta.yml") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == "__main__":
    size = int(sys.argv[1])
    data = pathlib.Path("corpus")
    meta = parse_meta()

    for ext in meta["formats"]:
        # Create a Hugo site for each format:
        subprocess.check_output(
            meta["commands"]["new"].format(dir=ext).split()
        ).decode("utf-8")

        # Populate the 'post' category with benchmark data:
        benchmark = (data / ("test." + ext)).read_text()
        for i in range(size):
            name = "test{0}.{1}".format(i, ext)
            with open("{0}/content/post/{1}".format(ext, name), "w+") as f:
                f.write(meta["layout"].format(content=benchmark))

    args = [
        "hyperfine",
        "--warmup",
        "3",
        "--max-runs",
        "5"
    ]

    for ext in meta["formats"]:
        args.append(meta["commands"]["build"].format(dir=ext))

    print(subprocess.check_output(args).decode("utf-8"))
