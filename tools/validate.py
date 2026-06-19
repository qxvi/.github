#!/usr/bin/env python3
import json
from pathlib import Path

root = Path.cwd()

required_files = [
    "README.md",
    "profile/README.md",
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "data/qxvi-surfaces.json",
    "data/qxvi-live-repository-registry.json",
    "docs/QXVI_PUBLIC_BOUNDARY_INTERFACE.md",
    "docs/QXVI_LIVE_SURFACE_AUDIT.md",
    "schemas/qxvi-org-control.schema.json"
]

for rel in required_files:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

json_files = [
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "data/qxvi-surfaces.json",
    "data/qxvi-live-repository-registry.json",
    "schemas/qxvi-org-control.schema.json"
]

for rel in json_files:
    json.loads((root / rel).read_text(encoding="utf-8"))

profile = (root / "profile/README.md").read_text(encoding="utf-8")
for token in ["qxvi","BOUNDARYCAM","What crossed the boundary?","The camera for machine action.","https://qxvi.github.io/BOUNDARYCAM","Repository surface list"]:
    if token not in profile:
        raise SystemExit("PROFILE_MISSING=" + token)

control = json.loads((root / "qxvi-org-control.json").read_text(encoding="utf-8"))
if control.get("state") != "QXVI_PUBLIC_BOUNDARY_INTERFACE_INDEXED":
    raise SystemExit("CONTROL_STATE_INVALID")

manifest = json.loads((root / "qxvi-org-manifest.json").read_text(encoding="utf-8"))
if manifest.get("version") != "0.2.0":
    raise SystemExit("MANIFEST_VERSION_INVALID")

registry = json.loads((root / "data/qxvi-live-repository-registry.json").read_text(encoding="utf-8"))
if registry.get("repo_count", 0) < 2:
    raise SystemExit("REPO_COUNT_TOO_LOW")

names = [r.get("nameWithOwner") for r in registry.get("repositories", [])]
for expected in ["qxvi/BOUNDARYCAM", "qxvi/.github"]:
    if expected not in names:
        raise SystemExit("MISSING_REPO=" + expected)

print("QXVI_ORG_VALIDATE_OK=true")
