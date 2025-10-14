import os
from pathlib import Path

RECIPES_DIR = Path("recipes")
TOC_FILE = Path("_toc.yml")
INDEX_FILE = Path("readme.md")

recipes = sorted(file for file in RECIPES_DIR.glob("*.md"))

# Build YAML content
content = []
content.append("format: jb-book")
content.append("root: readme\n")

# Preamble part
content.append("parts:")
content.append("  - caption: Preamble")
content.append("    chapters:")
content.append("    - file: preamble/foreword")
content.append("    - file: preamble/jupyter-book\n")

# Recipes part
content.append("  - caption: Recipes")
content.append("    chapters:")

for recipe in recipes:
    path = recipe.with_suffix("").as_posix()
    content.append(f"    - file: {path}")

# Write TOC
TOC_FILE.write_text("\n".join(content), encoding="utf-8")
print(f"_toc.yml updated with {len(recipes)} recipes.")
