.PHONY: bench build

all: bench

build:
	docker build -f Dockerfile -t jdkato/hyperfine:latest .
	docker tag jdkato/hyperfine:latest jdkato/hyperfine:latest
	docker push jdkato/hyperfine

	python scripts/build.py

bench:
	python scripts/main.py $(ssg)
