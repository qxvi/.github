import json
from pathlib import Path

root = Path.cwd()
state = "QXVI_OWNER_STACK_POWER_ROUTER_LIVE"

required = [
    "qxvi-owner-stack-power-router.json",
    "registry/qxvi-power-route-registry.json",
    "qxvi-owner-stack-accelerator.json",
    "midiakiasat-visible-owner-register.json",
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "docs/stack/QXVI_OWNER_STACK_POWER_ROUTER.md",
    "audit/QXVI_OWNER_STACK_POWER_ROUTER_AUDIT.md",
    "tools/power_router.py"
]

for rel in required:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

router = json.loads((root / "qxvi-owner-stack-power-router.json").read_text())
if router.get("state") != state:
    raise SystemExit("ROUTER_STATE_INVALID")

if len(router.get("routing_matrix", [])) < 6:
    raise SystemExit("ROUTES_TOO_FEW")

must = ["INVOCORDER", "Verifrax", "qxvi", "VATFix", "qvra", "TRUTHFRAMER", "ANTIMATTERIUM"]
all_sources = set()
for route in router.get("routing_matrix", []):
    all_sources.update(route.get("power_sources", []))
for name in must:
    if name not in all_sources:
        raise SystemExit("MISSING_POWER_SOURCE=" + name)

if "router_hash" not in router or "router_id" not in router:
    raise SystemExit("ROUTER_HASH_OR_ID_MISSING")

registry = json.loads((root / "registry/qxvi-power-route-registry.json").read_text())
if registry.get("router_hash") != router.get("router_hash"):
    raise SystemExit("REGISTRY_ROUTER_HASH_MISMATCH")

for rel in ["qxvi-org-control.json", "qxvi-org-manifest.json", "qxvi-org-completion.json"]:
    obj = json.loads((root / rel).read_text())
    if obj.get("state") != state:
        raise SystemExit("ORG_STATE_INVALID=" + rel)

print("QXVI_OWNER_STACK_POWER_ROUTER_VALIDATE_OK=true")
