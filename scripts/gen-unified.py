import sys, re

def getline(f):
	for line in f:
		line = line.strip()
		if line == "" or line.startswith("#"):
			continue
		return line
	return None

print "# Auto generated unified vectors"
print "<PinDef>"
print ",".join(["A%d"%i for i in range(24)] + ["Q%d"%i for i in range(24)])
print "</PinDef>"
print "<TestVector>"

for file in sys.argv[1:]:
	if not ("ripple" in file):
		with open(file, "r") as inf:
			assert getline(inf) == "<PinDef>"
			pins = [pin.strip() for pin in getline(inf).split(",")]
			assert getline(inf) == "</PinDef>"
			assert getline(inf) == "<TestVector>"
			while True:
				line = getline(inf)
				if line == "</TestVector>":
					break
				line = re.sub("\\s+", "", line)
				d = {}
				for i, pin in enumerate(pins):
					d[pin] = line[i]
				outline = ""
				for i in range(24):
					outline += d.get("A%d"%i, "0")
				outline += " "
				for i in range(24):
					outline += d.get("Q%d"%i, "X")
				print outline

print "</TestVector>"