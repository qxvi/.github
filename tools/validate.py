import json
from pathlib import Path

root = Path.cwd()
state = "QXVI_OWNER_STACK_ACCELERATOR_ARMED"

required = [
    "qxvi-owner-stack-accelerator.json",
    "midiakiasat-visible-owner-register.json",
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "docs/stack/QXVI_OWNER_STACK_ACCELERATOR.md",
    "audit/QXVI_OWNER_STACK_ACCELERATOR_AUDIT.md"
]

for rel in required:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

accel = json.loads((root / "qxvi-owner-stack-accelerator.json").read_text())
if accel.get("state") != state:
    raise SystemExit("ACCELERATOR_STATE_INVALID")

if len(accel.get("lanes", [])) < 10:
    raise SystemExit("LANES_TOO_FEW")

for required_owner in ["Verifrax", "VATFix", "INVOCORDER", "qxvi", "qvra", "TRUTHFRAMER", "ANTIMATTERIUM"]:
    if required_owner not in [lane.get("owner") for lane in accel.get("lanes", [])]:
        raise SystemExit("MISSING_POWER_LANE=" + required_owner)

for rel in ["qxvi-org-control.json", "qxvi-org-manifest.json", "qxvi-org-completion.json"]:
    obj = json.loads((root / rel).read_text())
    if obj.get("state") != state:
        raise SystemExit("ORG_STATE_INVALID=" + rel)

print("QXVI_OWNER_STACK_ACCELERATOR_VALIDATE_OK=true")
