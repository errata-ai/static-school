"""Record benchmark data for every SSG in 'generators'.
"""
import json
import os
import subprocess
import sys


if __name__ == "__main__":
    report = {}

    runs = sys.argv[1]
    for ssg in [f for f in os.listdir("generators") if not f.startswith(".")]:
        print("Benchmarking '{0}' ...".format(ssg))
        entry = subprocess.check_output([
            "docker",
            "run",
            "--rm",
            "hyperfine-" + ssg,
            runs
        ], cwd=os.path.abspath("generators/" + ssg))

        report[ssg] = json.loads(entry)

    with open("report.json", "w+") as f:
        json.dump(report, f)
