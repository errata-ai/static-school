"""Record benchmark data for every SSG in 'generators'.
"""
import json
import os
import subprocess
import sys
import urllib

GIST = "https://gist.githubusercontent.com/netlify-bot/{0}/raw/{1}".format(
    "99f2094783ddb2025bd1033f666c34cc", "staticgen-archive.json"
)


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


def find_stats(_id, stats):
    """Find the latest activity stats for the SSG with `_id`.
    """
    for ssg in stats:
        if ssg["id"] == _id:
            return ssg
    return None


def fetch_stats(ssg):
    """
    """
    resp = urllib.urlopen(GIST)
    return find_stats(ssg, json.loads(resp.read())[0][1])


if __name__ == "__main__":
    ssg = sys.argv[1]

    results = []
    for n in ["10", "100", "1000"]:
        print("Benchmarking '{0} ({1} files)' ...".format(ssg, n))

        entry = subprocess.check_output(
            ["docker", "run", "--rm", "hyperfine-" + ssg, n],
            cwd=os.path.abspath("generators/" + ssg),
        )
        results.append(json.loads(entry)["results"])

    results = format_results(results)

    print("Benchmarking completed; see `../data/report.json`.")
    write_report(ssg, {"data": results, "stats": fetch_stats(ssg)})
