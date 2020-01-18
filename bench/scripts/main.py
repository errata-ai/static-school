"""Record benchmark data for every SSG in 'generators'.
"""
import json
import os
import re
import subprocess
import sys

VERSION_RE = re.compile(r"v?\d+\.\d+\.\d+")


def write_report(ssg, results):
    """Write the `results` for `ssg` to disk.
    """
    p = "../data/report.json"

    with open(p, "r") as f:
        report = json.load(f)

    report[ssg]["data"] = results["data"]
    report[ssg]["version"] = results["version"]

    with open(p, "w+") as f:
        json.dump(report, f, indent=4)


def cmd_to_markup(cmd):
    """Find the type a markup from the given command.

    The idea is that, since our testing directories are named after a format --
    'md', 'adoc', or 'rst', we can infer the type of markup by looking for
    those strings in the build command -- e.g.,

    `cd {dir} && gatsby build && cd ..

    where `{dir}` would one of 'md', 'adoc', or 'rst'.
    """
    if "md" in cmd:
        return "Markdown"
    elif "adoc" in cmd:
        return "AsciiDoc"
    return "reStructuredText"


def format_results(results):
    """Format results into a Highcharts-friendly structure.
    """
    data = {}
    for run in results:
        for i, fmt in enumerate(run):
            name = cmd_to_markup(fmt["command"])
            if name in data:
                data[name].append(fmt["mean"])
            else:
                data[name] = [fmt["mean"]]
    return data


if __name__ == "__main__":
    ssg = sys.argv[1]

    results, version = [], None
    for n in ["10", "100", "1000"]:
        print("Benchmarking '{0} ({1} files)' ...".format(ssg, n))

        entry = subprocess.check_output(
            ["docker", "run", "--rm", "hyperfine-" + ssg, n],
            cwd=os.path.abspath("generators/" + ssg),
        )
        output = json.loads(entry)

        results.append(output["results"])

        version = VERSION_RE.search(output["version"])
        version = version.group(0)
        if not version.startswith("v"):
            version = "v" + version

    results = format_results(results)

    print("Benchmarking completed; see `../data/report.json`.")
    write_report(ssg, {"data": results, "version": version})
