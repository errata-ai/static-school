import pathlib
import sys

data = pathlib.Path("corpus")
text = pathlib.Path(sys.argv[1]).read_text()
path = sys.argv[2]
runs = int(sys.argv[3])

for ext in ["md", "adoc", "rst"]:
    benchmark = (data / ("test." + ext)).read_text()
    for i in range(runs):
        name = "test{0}.{1}".format(i, ext)
        with open(path.format(ext, name), "w+") as f:
            f.write(text.format(content=benchmark))
