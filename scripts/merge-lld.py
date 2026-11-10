#!/usr/bin/env python3
"""Joins the experts' LLD parts in template order and reports gaps. Uses no tokens."""
import glob
import os
import re
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
topic_dir = os.path.abspath(sys.argv[1]).rstrip("/")
topic = os.path.basename(topic_dir)
template = open(os.path.join(root, "skills/architecture-work/templates/lld.md"), encoding="utf-8").read()
required = re.findall(r"^## (.+)$", template, re.M)
found = {}
problems = []
for path in sorted(glob.glob(os.path.join(topic_dir, "parts", "*.md"))):
    name = os.path.basename(path)
    parts = re.split(r"^## (.+)$", open(path, encoding="utf-8").read(), flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        heading, body = parts[i].strip(), parts[i + 1].strip()
        if heading not in required:
            problems.append(f"unknown section in {name}: {heading}")
        elif heading in found:
            problems.append(f"section written twice: {heading} ({found[heading][0]}, {name})")
        else:
            found[heading] = (name, body)
problems += [f"missing section: {h}" for h in required if h not in found]
problems += [f"empty section: {h} ({found[h][0]})" for h in required if h in found and not found[h][1]]
for problem in problems:
    print(f"FAIL {problem}")
if problems:
    sys.exit(1)
target = os.path.join(os.path.dirname(topic_dir), f"{topic}-lld.md")
text = f"# LLD: {topic}\n\n" + "\n\n".join(f"## {h}\n\n{found[h][1]}" for h in required) + "\n"
open(target, "w", encoding="utf-8").write(text)
print(f"OK {target}: {len(required)} sections from {len({v[0] for v in found.values()})} parts")
