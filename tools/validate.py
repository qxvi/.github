#!/usr/bin/env python3
import json
from pathlib import Path

root = Path.cwd()
required_files = ["README.md","profile/README.md","qxvi-org-control.json","qxvi-org-manifest.json","data/qxvi-surfaces.json","docs/QXVI_PUBLIC_BOUNDARY_INTERFACE.md","schemas/qxvi-org-control.schema.json"]

for rel in required_files:
    path = root / rel
    if not path.exists():
        raise SystemExit("MISSING_FILE=" + rel)

for rel in ["qxvi-org-control.json","qxvi-org-manifest.json","data/qxvi-surfaces.json","schemas/qxvi-org-control.schema.json"]:
    json.loads((root / rel).read_text(encoding="utf-8"))

profile = (root / "profile/README.md").read_text(encoding="utf-8")
for token in ["qxvi","BOUNDARYCAM","What crossed the boundary?","The camera for machine action.","https://qxvi.github.io/BOUNDARYCAM"]:
    if token not in profile:
        raise SystemExit("PROFILE_MISSING=" + token)

control = json.loads((root / "qxvi-org-control.json").read_text(encoding="utf-8"))
if control.get("state") != "QXVI_PUBLIC_BOUNDARY_INTERFACE_OPEN":
    raise SystemExit("CONTROL_STATE_INVALID")

manifest = json.loads((root / "qxvi-org-manifest.json").read_text(encoding="utf-8"))
if manifest.get("version") != "0.1.0":
    raise SystemExit("MANIFEST_VERSION_INVALID")

print("QXVI_ORG_VALIDATE_OK=true")
