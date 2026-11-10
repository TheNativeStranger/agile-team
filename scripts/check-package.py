#!/usr/bin/env python3
"""Checks that a job's full architecture package is complete. Uses no tokens."""
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

scripts = os.path.dirname(os.path.abspath(__file__))
topic = sys.argv[1]
base = sys.argv[2] if len(sys.argv) > 2 else "docs/architecture"
problems = []
path = lambda *p: os.path.join(base, *p)


def need(p):
    if not os.path.exists(p):
        problems.append(f"missing file: {p}")
        return False
    return True


need(path("input", topic, "index.md"))
need(path("decisions", f"{topic}.md"))
grooming = path("grooming", f"{topic}.md")
if need(grooming) and not re.search(r"^## Onay\s*\n+\s*\S", open(grooming, encoding="utf-8").read(), re.M):
    problems.append("grooming record has no approval under '## Onay'")
PAGES = {"mimari": ["Bağlam", "Bileşen", "Entegrasyon", "Dağıtım"], "tasarim": ["Sequence", "Sınıf", "Veri", "Olay"]}
for kind, required in PAGES.items():
    drawing = path("diagrams", f"{topic}-{kind}.drawio")
    if need(drawing):
        result = subprocess.run([sys.executable, os.path.join(scripts, "check-drawio.py"), drawing], capture_output=True, text=True)
        if result.returncode:
            problems.append(result.stdout.strip())
        else:
            names = [d.get("name", "") for d in ET.parse(drawing).getroot().findall("diagram")]
            problems += [f"{kind} drawing has no '{r}' page" for r in required if not any(r.lower() in n.lower() for n in names)]
for kind, drawing in (("hld", "mimari"), ("lld", "tasarim")):
    doc = path(kind, f"{topic}-{kind}.md")
    if need(doc):
        result = subprocess.run([sys.executable, os.path.join(scripts, "check-docs.py"), doc, "--type", kind], capture_output=True, text=True)
        if result.returncode:
            problems += [l for l in result.stdout.splitlines() if l.startswith("FAIL") and doc not in l]
        if f"{topic}-{drawing}.drawio" not in open(doc, encoding="utf-8").read():
            problems.append(f"{kind} does not link {topic}-{drawing}.drawio")
for problem in problems:
    print(f"FAIL {problem}")
print(("OK" if not problems else "FAIL") + f" {topic}: {'package complete' if not problems else str(len(problems)) + ' problem(s)'}")
sys.exit(1 if problems else 0)
