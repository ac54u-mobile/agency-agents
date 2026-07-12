# CC Pocket integration

This directory exposes a small, stable, Chinese-localized catalog for
`ac54u-mobile/cc-pocket`. It is intentionally curated for coding sessions instead of
shipping the entire Agency roster into a mobile `@` picker.

- `catalog.zh-CN.json` is the maintained source metadata.
- `dist/agents.zh-CN.json` is the generated manifest consumed by CC Pocket.
- Every generated entry contains a stable ID, Chinese display metadata, source path,
  raw-content URL, and SHA-256 digest.

Regenerate and validate after changing an agent source or catalog entry:

```bash
python3 scripts/build-cc-pocket-catalog.py
git diff --check
```

CC Pocket should cache the generated manifest and agent Markdown. A cached Markdown
file is accepted only when its SHA-256 matches the manifest. The repository remains
MIT licensed; downstream distributions must retain the repository's license notice.
