import datetime
import pathlib
import json

import bs4
import frontmatter
import requests
import timeago
import yaml

from ruamel.yaml import YAML as ryaml
from user_agent import generate_user_agent

R_YAML = ryaml()
R_YAML.preserve_quotes = True

GIST = "https://gist.githubusercontent.com/netlify-bot/{0}/raw/{1}".format(
    "99f2094783ddb2025bd1033f666c34cc", "staticgen-archive.json"
)

ISSUES = "https://isitmaintained.com/project/{0}"
COMMIT = "https://api.github.com/repos/{0}/commits/master"
RELEASE = "https://api.github.com/repos/{0}/releases"
REPO = "https://api.github.com/repos/{0}"

# Get latest version from NPM instead of GitHub:
#
# This is required for repos that don't pubished GitHub releases.
NPM = [
    "gatsby"
]


def fetch_github_stats(data_file):
    """Fetch GitHub-related stats for the given data file.
    """
    with open(data_file, "r") as f:
        data = R_YAML.load(f)

    options = []
    for entry in data["options"]:
        repo = entry.get("repo")
        if repo:
            info = requests.get(REPO.format(repo)).json()
            entry["metrics"] = {
                'stars': info["stargazers_count"],
                'issues': info["open_issues"]
            }
        options.append(entry)

    data["options"] = options
    with open(data_file, "w+") as f:
        R_YAML.dump(data, f)


def find_stats(_id, stats):
    """Find the latest activity stats for the SSG with `_id`.
    """
    for ssg in stats:
        if ssg["id"] == _id:
            return ssg
    return None


def update_stats():
    """Find the latest activity stats for the SSG with `_id`.
    """
    now = datetime.datetime.now()

    p = "../data/report.json"
    with open(p, "r") as f:
        report = json.load(f)

    perf = {}
    resp = requests.get(GIST)
    data = resp.json()[0][1]

    for entry in pathlib.Path("../content/ssg").glob("**/*.md"):
        meta, _ = frontmatter.parse(entry.read_text())

        ssg = meta["title"].lower()
        print("Recording stats for '{0}' ...".format(ssg))

        perf[ssg] = meta["language"]

        # Netlify-recorded stats:
        report[ssg]["stats"] = find_stats(ssg, data)

        # Is it maintained?
        resp = requests.get(
            ISSUES.format(meta["repo"]),
            headers={"User-Agent": generate_user_agent()},
        )
        soup = bs4.BeautifulSoup(resp.text, features="lxml")
        resu = soup.find("strong", {"class": "text-primary"})

        # GitHub
        resp = requests.get(COMMIT.format(meta["repo"]))

        date = resp.json()["commit"]["author"]["date"]
        d1 = datetime.datetime.strptime(date.split("T")[0], "%Y-%m-%d")

        if ssg in NPM:
            resp = requests.get(
                "https://www.npmjs.com/package/" + ssg,
                headers={"User-Agent": generate_user_agent()},
            )
            soup = bs4.BeautifulSoup(resp.text, features="lxml")
            time = soup.find("time", {})
            r_date = time.text
        else:
            resp = requests.get(RELEASE.format(meta["repo"]))
            date = resp.json()[0]["published_at"]
            d2 = datetime.datetime.strptime(date.split("T")[0], "%Y-%m-%d")
            r_date = timeago.format(d2, now)

        report[ssg]["metrics"] = {
            "resolution": resu.text,
            "commit": timeago.format(d1, now),
            "release": r_date,
        }

    # Markup Performance
    for ssg, lang in perf.items():
        ranks = {}
        for fmt in ["Markdown", "AsciiDoc", "reStructuredText"]:
            if fmt not in report[ssg]["data"]:
                continue

            # We use the recorded time from the largest size (1,000) files:
            t1 = report[ssg]["data"][fmt][2]
            rank = 1

            for other in report:
                other_data = report[other]["data"]
                if other == ssg or fmt not in other_data:
                    continue
                elif other_data[fmt][2] < t1:
                    rank += 1

            ranks[fmt] = rank

        report[ssg]["performace"] = ranks

    with open(p, "w+") as f:
        json.dump(report, f, indent=4)


if __name__ == "__main__":
    update_stats()

    data = pathlib.Path("../data/tools").resolve()
    for p in data.glob("*.yml"):
        print("Fetching stats for {0}".format(p.name))
        fetch_github_stats(str(p))
