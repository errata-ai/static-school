import datetime
import pathlib
import json

import bs4
import frontmatter
import requests
import timeago

from user_agent import generate_user_agent

GIST = "https://gist.githubusercontent.com/netlify-bot/{0}/raw/{1}".format(
    "99f2094783ddb2025bd1033f666c34cc", "staticgen-archive.json"
)
ISSUES = "https://isitmaintained.com/project/{0}"
COMMIT = "https://api.github.com/repos/{0}/commits/master"
RELEASE = "https://api.github.com/repos/{0}/releases"


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

        resp = requests.get(RELEASE.format(meta["repo"]))
        date = resp.json()[0]["published_at"]
        d2 = datetime.datetime.strptime(date.split("T")[0], "%Y-%m-%d")

        report[ssg]["metrics"] = {
            "resolution": resu.text,
            "commit": timeago.format(d1, now),
            "release": timeago.format(d2, now),
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
