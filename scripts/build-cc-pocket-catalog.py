#!/usr/bin/env python3
"""Build the complete Chinese CC Pocket @-agent manifest."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "integrations/cc-pocket/catalog.zh-CN.json"
OUTPUT = ROOT / "integrations/cc-pocket/dist/agents.zh-CN.json"
CATEGORY_ZH = {
    "academic": "学术", "design": "设计", "engineering": "工程", "finance": "财务",
    "game-development": "游戏开发", "gis": "地理信息", "healthcare": "医疗",
    "marketing": "市场营销", "paid-media": "付费媒体", "product": "产品",
    "project-management": "项目管理", "sales": "销售", "security": "安全",
    "spatial-computing": "空间计算", "specialized": "专业服务", "support": "支持",
    "testing": "测试",
}

def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result

config = json.loads(CONFIG.read_text(encoding="utf-8"))
source_root = ROOT / config["sourceRoot"]
excluded = set(config.get("exclude", []))
agents = []
ids = set()
for source in sorted(source_root.rglob("*.md")):
    rel_locale = source.relative_to(source_root)
    if rel_locale.name in excluded:
        continue
    text = source.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if not meta.get("name") or not meta.get("description"):
        continue
    rel = source.relative_to(ROOT).as_posix()
    slug = re.sub(r"[^a-z0-9]+", "-", rel_locale.with_suffix("").as_posix().lower()).strip("-")
    if slug in ids:
        raise SystemExit(f"duplicate agent id: {slug}")
    ids.add(slug)
    top = rel_locale.parts[0]
    english = ROOT / rel_locale
    agents.append({
        "id": slug,
        "nameZh": meta["name"],
        "summaryZh": meta["description"],
        "category": top,
        "categoryZh": CATEGORY_ZH.get(top, top),
        "emoji": meta.get("emoji"),
        "source": rel,
        "englishSource": rel_locale.as_posix() if english.is_file() else None,
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "rawUrl": f"https://raw.githubusercontent.com/{config['sourceRepository']}/main/{rel}",
    })

manifest = {**config, "agentCount": len(agents), "agents": agents}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(agents)} agents)")
