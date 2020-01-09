"""Record benchmark data for every SSG in 'generators'.
"""
import json
import os
import subprocess
import sys


def write_report(ssg, results):
    """
    """
    p = "../data/report.json"

    with open(p, "r") as f:
        report = json.load(f)

    report[ssg] = results

    with open(p, "w+") as f:
        json.dump(report, f, indent=4)


def cmd_to_markup(cmd):
    """
    """
    if "md" in cmd:
        return "Markdown"
    elif "adoc" in cmd:
        return "AsciiDoc"
    return "reStructuredText"


def format_results(results):
    """
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
        version = output["version"]

    results = format_results(results)

    print("Benchmarking completed; see `../data/report.json`.")
    write_report(ssg, {"data": results, "version": version})
