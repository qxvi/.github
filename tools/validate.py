import json
from pathlib import Path

root = Path.cwd()

required = [
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "qxvi-whole-stack-integrity-lock.json",
    "data/live/boundarycam/boundarycam-manifest.v0.7.0.json",
    "data/live/boundarycam/boundarycam-public-control.v0.7.0.json",
    "data/live/boundarycam/boundarycam-completion.v0.7.0.json",
    "data/live/boundarycam/boundarycam-whole-stack-integrity.v0.7.0.json",
    "data/live/boundarycam/release.v0.7.0.json",
    "data/live/boundarycam/verify.v0.7.0.json",
    "docs/stack/QXVI_WHOLE_STACK_INTEGRITY_LOCK.md",
    "audit/QXVI_WHOLE_STACK_INTEGRITY_AUDIT.md"
]

for rel in required:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

state = json.loads((root / "qxvi-whole-stack-integrity-lock.json").read_text())
if state.get("state") != "QXVI_WHOLE_STACK_INTEGRITY_LOCKED":
    raise SystemExit("QXVI_STATE_INVALID")

bc = state.get("boundarycam", {})
if bc.get("state") != "BOUNDARYCAM_WHOLE_STACK_INTEGRITY_LOCKED":
    raise SystemExit("BOUNDARYCAM_STATE_INVALID")
if bc.get("verify_conclusion") != "success":
    raise SystemExit("BOUNDARYCAM_VERIFY_INVALID")

for rel in ["qxvi-org-control.json", "qxvi-org-manifest.json", "qxvi-org-completion.json"]:
    obj = json.loads((root / rel).read_text())
    if obj.get("state") != "QXVI_WHOLE_STACK_INTEGRITY_LOCKED":
        raise SystemExit("ORG_OBJECT_STATE_INVALID=" + rel)

print("QXVI_V060_WHOLE_STACK_VALIDATE_OK=true")
