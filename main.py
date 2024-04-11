import io
import pprint

f = io.open("get.txt", mode="r", encoding="utf-8")

text = f.read()

lines = text.split('\n')

for i, l in enumerate(lines): lines[i] += "\n"

new_lines = []

for l in lines:
	if len(l) > 19:
		for i in range(len(l) // 19):
			new_lines.append(l[i * 19:(i + 1) * 19])
		if len(l) % 19 != 0:
			new_lines.append(l[(len(l) // 19) * 19:])
	else:
		new_lines.append(l)

pprint.pp(lines)
pprint.pp(new_lines)

pages = []
t = ""
c = 0
for l in new_lines:
	c += len(l)
	if c < 256:
		t += l
	else:
		pages.append(t)
		t = ""
		c = 0

pprint.pp(pages)
	
with open("out.txt", "w", encoding="utf-8") as f:
	for p in pages:
		f.write(p)