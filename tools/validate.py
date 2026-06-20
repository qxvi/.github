import json
from pathlib import Path

root = Path.cwd()
state = "QXVI_WHOLE_ALL_OWNER_STACK_REGISTERED"

required = [
    "midiakiasat-visible-owner-register.json",
    "qxvi-whole-all-owner-stack.json",
    "qxvi-org-control.json",
    "qxvi-org-manifest.json",
    "qxvi-org-completion.json",
    "docs/stack/QXVI_WHOLE_ALL_OWNER_STACK_REGISTER.md",
    "audit/QXVI_WHOLE_ALL_OWNER_STACK_AUDIT.md",
]

owners = [
    "verifrax",
    "vatfix",
    "qvra",
    "invocorder",
    "antimatterium",
    "kaaffilm",
    "truthframer",
    "qxvi",
    "cinematicum",
    "qxvo",
    "qzro",
    "aikido-bounty-lab",
    "qvro",
    "qvru",
    "qxra",
    "qzru",
]

for rel in required:
    if not (root / rel).exists():
        raise SystemExit("MISSING_FILE=" + rel)

for owner in owners:
    path = root / "data/live/owners" / f"{owner}.repos.json"
    if not path.exists():
        raise SystemExit("MISSING_OWNER_REPOS=" + owner)
    json.loads(path.read_text())

register = json.loads((root / "midiakiasat-visible-owner-register.json").read_text())
whole = json.loads((root / "qxvi-whole-all-owner-stack.json").read_text())

if register.get("state") != state:
    raise SystemExit("REGISTER_STATE_INVALID")
if whole.get("state") != state:
    raise SystemExit("WHOLE_STATE_INVALID")
if register.get("owner_count") != 16:
    raise SystemExit("OWNER_COUNT_INVALID")
if whole.get("register_hash") != register.get("register_hash"):
    raise SystemExit("REGISTER_HASH_MISMATCH")

for rel in ["qxvi-org-control.json", "qxvi-org-manifest.json", "qxvi-org-completion.json"]:
    obj = json.loads((root / rel).read_text())
    if obj.get("state") != state:
        raise SystemExit("ORG_STATE_INVALID=" + rel)

print("QXVI_WHOLE_ALL_OWNER_STACK_VALIDATE_OK=true")
