#!/bin/sh
set -e

MD="hugo -D --config=md/config.toml --contentDir=md/content"
ADOC="hugo -D --config=adoc/config.toml --contentDir=adoc/content"
RST="hugo -D --config=rst/config.toml --contentDir=rst/content"

hyperfine --warmup 3 --max-runs 5 "$MD" "$ADOC" "$RST"
