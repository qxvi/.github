#!/usr/bin/env python3
import json
from pathlib import Path

root = Path.cwd()

required_files = [
    "README.md",
    "profile/README.md",
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "qxvi-boundarycam-completion-propagation.json",
    "data/qxvi-surfaces.json",
    "data/qxvi-live-repository-registry.json",
    "data/live/boundarycam/boundarycam-completion.live.json",
    "docs/QXVI_PUBLIC_BOUNDARY_INTERFACE.md",
    "docs/QXVI_LIVE_SURFACE_AUDIT.md",
    "docs/QXVI_ORG_CHARTER.md",
    "docs/QXVI_OPERATIONAL_DOCTRINE.md",
    "docs/QXVI_BOUNDARYCAM_COMPLETION_PROPAGATION.md",
    "governance/GOVERNANCE.md",
    "security/SECURITY.md",
    "support/SUPPORT.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/boundary-surface.yml",
    ".github/ISSUE_TEMPLATE/control-gap.yml",
    "schemas/qxvi-org-control.schema.json"
]

for rel in required_files:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

json_files = [
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "qxvi-boundarycam-completion-propagation.json",
    "data/qxvi-surfaces.json",
    "data/qxvi-live-repository-registry.json",
    "data/live/boundarycam/boundarycam-completion.live.json",
    "schemas/qxvi-org-control.schema.json"
]

for rel in json_files:
    json.loads((root / rel).read_text(encoding="utf-8"))

propagation = json.loads((root / "qxvi-boundarycam-completion-propagation.json").read_text(encoding="utf-8"))
if propagation.get("state") != "QXVI_BOUNDARYCAM_COMPLETION_PROPAGATED":
    raise SystemExit("PROPAGATION_STATE_INVALID")

bc = propagation.get("boundarycam", {})
if bc.get("completion_state") != "BOUNDARYCAM_PRODUCT_CONTROL_STACK_COMPLETE":
    raise SystemExit("BOUNDARYCAM_COMPLETION_NOT_PROPAGATED")

control = json.loads((root / "qxvi-org-control.json").read_text(encoding="utf-8"))
if control.get("state") != "QXVI_BOUNDARYCAM_COMPLETION_PROPAGATED":
    raise SystemExit("CONTROL_STATE_INVALID")

manifest = json.loads((root / "qxvi-org-manifest.json").read_text(encoding="utf-8"))
if manifest.get("version") != "0.4.0":
    raise SystemExit("MANIFEST_VERSION_INVALID")

print("QXVI_V040_PROPAGATION_VALIDATE_OK=true")
