import json
import os
import subprocess
import sys


if __name__ == "__main__":
    for ssg in [f for f in os.listdir("generators") if not f.startswith(".")]:
        print("Building '{0}' ...".format(ssg))
        subprocess.check_output([
            "docker",
            "build",
            "-f",
            "Dockerfile",
            "-t",
            "hyperfine-{0}:latest".format(ssg),
            "."
        ], cwd=os.path.abspath("generators/" + ssg))
