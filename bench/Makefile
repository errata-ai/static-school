.PHONY: bench build push stats

all: bench

push:
	docker build -f Dockerfile -t jdkato/hyperfine:latest .
	docker tag jdkato/hyperfine:latest jdkato/hyperfine:latest
	docker push jdkato/hyperfine

build:
	python scripts/build.py

bench:
	python scripts/main.py $(ssg)

stats:
	python scripts/stats.py
