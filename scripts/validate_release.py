from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8-sig")

errors = []
if not text.startswith("---\n"):
    errors.append("missing YAML frontmatter")
for field in ("name:", "description:"):
    if field not in text.split("---", 2)[1]:
        errors.append(f"missing frontmatter field: {field}")

match = re.search(r"^name:\s*([^\n]+)$", text, re.M)
if not match or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", match.group(1).strip()):
    errors.append("skill name must use lowercase letters, numbers, and hyphens")

for relative in (
    "references/workflow.md",
    "references/output-spec.md",
    "references/isolation-and-evidence.md",
    "tests/pressure-scenarios.md",
):
    if not (ROOT / relative).exists():
        errors.append(f"missing required file: {relative}")

for forbidden in ("F:\\2027考研资料", "徐丽丹", "wencker", "本人_wencker"):
    if forbidden.lower() in text.lower():
        errors.append(f"public package contains private identifier: {forbidden}")

required_phrases = (
    "个人错题",
    "考生隔离",
    "题库真实题量",
    "真题原文",
    "回访清单",
)
for phrase in required_phrases:
    if phrase not in text:
        errors.append(f"missing core instruction: {phrase}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    raise SystemExit(1)

print("OK: release skill structure and privacy checks passed")
