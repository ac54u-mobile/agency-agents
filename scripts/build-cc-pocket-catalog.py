#!/usr/bin/env python3
"""Build the stable, directly consumable CC Pocket agent manifest."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "integrations/cc-pocket/catalog.zh-CN.json"
OUTPUT = ROOT / "integrations/cc-pocket/dist/agents.zh-CN.json"

catalog = json.loads(SOURCE.read_text(encoding="utf-8"))
seen = set()
for agent in catalog["agents"]:
    agent_id = agent["id"]
    if agent_id in seen:
        raise SystemExit(f"duplicate agent id: {agent_id}")
    seen.add(agent_id)
    source = ROOT / agent["source"]
    if not source.is_file():
        raise SystemExit(f"missing source for {agent_id}: {agent['source']}")
    body = source.read_bytes()
    agent["sha256"] = hashlib.sha256(body).hexdigest()
    agent["rawUrl"] = (
        "https://raw.githubusercontent.com/"
        f"{catalog['sourceRepository']}/main/{agent['source']}"
    )

catalog["agentCount"] = len(catalog["agents"])
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {OUTPUT.relative_to(ROOT)} ({catalog['agentCount']} agents)")
