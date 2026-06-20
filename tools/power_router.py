import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
router = json.loads((root / "qxvi-owner-stack-power-router.json").read_text())

print("QXVI_OWNER_STACK_POWER_ROUTER_LIVE=true")
print("ROUTER_ID=" + router["router_id"])
print("ROUTER_HASH=" + router["router_hash"])
print("")
print("PRIORITY_EXECUTION_ORDER")
for item in router["priority_execution_order"]:
    print(str(item["rank"]) + ". " + item["move"] + " :: " + item["reason"])
print("")
print("ROUTES")
for route in router["routing_matrix"]:
    print("- " + route["output"] + " <= " + " + ".join(route["power_sources"]))
