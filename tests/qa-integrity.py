#!/usr/bin/env python3
"""Static integrity QA for the coach skill. Verifies the routing graph resolves.
Run from the skill root: python3 tests/qa-integrity.py"""
import os,re,glob,sys

FAIL=[]; WARN=[]
def fail(m): FAIL.append(m)
def warn(m): WARN.append(m)
def read(p):
    try: return open(p,encoding="utf-8").read()
    except FileNotFoundError: return None

coach=read("COACH.md") or ""
skill=read("SKILL.md") or ""
cmd_files={os.path.basename(f)[:-3] for f in glob.glob("references/commands/*.md")}
ref_files={os.path.basename(f)[:-3] for f in glob.glob("references/*.md")}

# 1. registry rows <-> files
registry=set(re.findall(r'^\|\s*`([a-z\-]+)(?:\s+\[[^\]]*\])?`', coach, re.M))
for c in sorted(registry-cmd_files): fail(f"registry lists `{c}` but references/commands/{c}.md is missing")
for c in sorted(cmd_files-registry): warn(f"references/commands/{c}.md exists but is not in the COACH.md registry")

# 2. SKILL.md description <-> files
desc=re.search(r'Activates for any coaching command:(.+?)(?:\.|Note:)', skill, re.S)
if desc:
    named={w.strip() for w in desc.group(1).replace("\n"," ").split(",") if w.strip()}
    for c in sorted(named-cmd_files-{''}): fail(f"SKILL.md advertises `{c}` but no command file exists")

# 3. every references/X.md path mentioned anywhere resolves
allmd=glob.glob("references/**/*.md",recursive=True)+["COACH.md","SKILL.md","README.md"]
for f in allmd:
    t=read(f) or ""
    for p in set(re.findall(r'references/(?:commands/)?([a-z0-9\-]+)\.md', t)):
        if p not in ref_files and p not in cmd_files and p!="commands":
            fail(f"{f} -> references/.../{p}.md does not exist")

# 4. state files referenced by commands exist
for f in allmd:
    t=read(f) or ""
    for p in set(re.findall(r'`([a-z_0-9]+\.md)`', t)):
        if p.startswith("coaching_state") or p in ("storybank.md","loops.md","history.md"):
            if not os.path.exists(p): fail(f"{f} -> `{p}` does not exist at skill root")

# 5. state section headers referenced as "### Section" / "## Section" by commands
state=read("coaching_state.md") or ""
heads={h.strip("# ").strip().lower() for h in re.findall(r'^#{2,3} .+$', state, re.M)}
for key in ["profile","storybank","score history","outcome log","interview loops (active)",
            "active coaching strategy","coaching notes","session log","interview intelligence"]:
    if not any(key in h for h in heads): fail(f"coaching_state.md is missing expected section: {key}")

# 6. DERIVED markers paired
for name in set(re.findall(r'DERIVED:([a-z_]+) START', state)):
    if state.count(f"DERIVED:{name} START")!=state.count(f"DERIVED:{name} END"):
        fail(f"DERIVED:{name} markers unbalanced in coaching_state.md")

# 7. storybank ID integrity
ids=set(re.findall(r'^\|\s*(S\d{3})\s*\|', state, re.M))
sb=read("storybank.md")
if sb: ids |= set(re.findall(r'^\|\s*(S\d{3})\s*\|', sb, re.M))
refd=set(re.findall(r'\b(S\d{3})\b', state))
for i in sorted(refd-ids): warn(f"story {i} is referenced in state but has no index row")
print(f"storybank index: {len(ids)} stories")

# 8. README documents every command (catches doc drift after a refactor)
rd=read("README.md") or ""
readme=set(re.findall(r'^\|\s*`([a-z\-]+)', rd, re.M))
for c in sorted(cmd_files-readme): fail(f"references/commands/{c}.md exists but README.md does not document it")
for c in sorted(readme-cmd_files-registry): warn(f"README.md documents `{c}` but no command file exists")

print(f"commands: {len(cmd_files)} files, {len(registry)} in registry")
print(f"\n{len(FAIL)} FAIL / {len(WARN)} WARN")
for m in FAIL: print("  FAIL:", m)
for m in WARN: print("  warn:", m)
sys.exit(1 if FAIL else 0)
