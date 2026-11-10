#!/usr/bin/env python3
"""Checks an HLD, LLD or ADR against its template. Uses no tokens."""
import argparse
import os
import re
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parser = argparse.ArgumentParser()
parser.add_argument("document")
parser.add_argument("--type", choices=["hld", "lld", "adr"], required=True)
args = parser.parse_args()

template = open(os.path.join(root, "skills/architecture-work/templates", f"{args.type}.md"), encoding="utf-8").read()
required = re.findall(r"^## (.+)$", template, re.M)
text = open(args.document, encoding="utf-8").read()
parts = re.split(r"^## (.+)$", text, flags=re.M)
sections = {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}
base = os.path.dirname(os.path.abspath(args.document))
problems = [f"missing section: {name}" for name in required if name not in sections]
problems += [f"empty section: {name}" for name in required if name in sections and not sections[name]]
for link in re.findall(r"\]\(([^)#]+\.drawio)\)", text):
    if not link.startswith("http") and not os.path.exists(os.path.join(base, link)):
        problems.append(f"broken diagram link: {link}")
open_marks = len(re.findall(r"\bTBD\b|<[^<>\n]{1,40}>", text))
for problem in problems:
    print(f"FAIL {problem}")
print(f"{'OK' if not problems else 'FAIL'} {args.document}: {len(required) - sum(p.startswith(('missing', 'empty')) for p in problems)}/{len(required)} sections, {open_marks} placeholder(s)")
sys.exit(1 if problems else 0)
