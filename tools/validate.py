import json
from pathlib import Path

root = Path.cwd()
state = "QXVI_ROUTE_ONE_INVOCORDER_BOUNDARYCAM_EXECUTED"

required = [
    "qxvi-route-one-invocorder-boundarycam.json",
    "registry/routes/route-001-invocorder-boundarycam.json",
    "data/live/boundarycam/boundarycam-manifest.v0.8.0.json",
    "data/live/boundarycam/boundarycam-public-control.v0.8.0.json",
    "data/live/boundarycam/boundarycam-completion.v0.8.0.json",
    "data/live/boundarycam/invocorder-boundarycam-route.v0.8.0.json",
    "data/live/boundarycam/invocorder-boundarycam-capture-contract.v0.8.0.json",
    "data/live/boundarycam/release.v0.8.0.json",
    "data/live/boundarycam/verify.v0.8.0.json",
    "docs/stack/QXVI_ROUTE_ONE_INVOCORDER_BOUNDARYCAM.md",
    "audit/QXVI_ROUTE_ONE_INVOCORDER_BOUNDARYCAM_AUDIT.md",
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json"
]

for rel in required:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

execution = json.loads((root / "qxvi-route-one-invocorder-boundarycam.json").read_text())
if execution.get("state") != state:
    raise SystemExit("EXECUTION_STATE_INVALID")
if execution.get("boundarycam", {}).get("verify_conclusion") != "success":
    raise SystemExit("BOUNDARYCAM_VERIFY_INVALID")

for rel in ["qxvi-org-control.json", "qxvi-org-manifest.json", "qxvi-org-completion.json"]:
    obj = json.loads((root / rel).read_text())
    if obj.get("state") != state:
        raise SystemExit("ORG_STATE_INVALID=" + rel)

print("QXVI_ROUTE_ONE_VALIDATE_OK=true")
