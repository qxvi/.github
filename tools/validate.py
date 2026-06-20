import json
from pathlib import Path

root = Path.cwd()

required = [
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "qxvi-whole-stack-state.json",
    "data/live/boundarycam/boundarycam-manifest.v0.6.0.json",
    "data/live/boundarycam/boundarycam-public-control.v0.6.0.json",
    "data/live/boundarycam/boundarycam-completion.v0.6.0.json",
    "data/live/boundarycam/release.v0.6.0.json",
    "data/live/boundarycam/verify.v0.6.0.json",
    "docs/stack/QXVI_WHOLE_STACK_EVIDENCE_BUNDLE_PROPAGATION.md",
    "audit/QXVI_WHOLE_STACK_AUDIT.md"
]

for rel in required:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

state = json.loads((root / "qxvi-whole-stack-state.json").read_text())
if state.get("state") != "QXVI_WHOLE_STACK_EVIDENCE_BUNDLE_PROPAGATED":
    raise SystemExit("WHOLE_STACK_STATE_INVALID")

bc = state.get("boundarycam", {})
if bc.get("state") != "BOUNDARYCAM_EVIDENCE_BUNDLE_CORE_OPEN":
    raise SystemExit("BOUNDARYCAM_STATE_NOT_PROPAGATED")
if bc.get("verify_conclusion") != "success":
    raise SystemExit("BOUNDARYCAM_VERIFY_NOT_SUCCESS")

for rel in ["qxvi-org-control.json", "qxvi-org-manifest.json", "qxvi-org-completion.json"]:
    obj = json.loads((root / rel).read_text())
    if obj.get("state") != "QXVI_WHOLE_STACK_EVIDENCE_BUNDLE_PROPAGATED":
        raise SystemExit("ORG_OBJECT_NOT_PROPAGATED=" + rel)

print("QXVI_WHOLE_STACK_VALIDATE_OK=true")
