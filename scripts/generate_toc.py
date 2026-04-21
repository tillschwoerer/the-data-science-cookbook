import os
from pathlib import Path
from collections import defaultdict

RECIPES_DIR = Path("recipes")
TOC_FILE = Path("_toc.yml")

recipes = sorted(file for file in RECIPES_DIR.rglob("*.md") if file.name not in ("readme.md", "index.md"))

# Group by season
seasons = defaultdict(list)
for recipe in recipes:
    season = recipe.parts[1]
    seasons[season].append(recipe)

# Build YAML content
content = []
content.append("format: jb-book")
content.append("root: readme\n")

content.append("parts:")
content.append("  - caption: Preamble")
content.append("    chapters:")
content.append("    - file: preamble/foreword")

for season in sorted(seasons):
    title = season.replace("-", " ").title()
    content.append(f"  - caption: {title}")
    content.append(f"    chapters:")
    for recipe in seasons[season]:
        path = recipe.with_suffix("").as_posix()
        content.append(f"    - file: {path}")
    content.append("")

content.append("  - caption: Epilogue")
content.append("    chapters:")
content.append("    - file: epilogue/jupyter-book\n")    

TOC_FILE.write_text("\n".join(content), encoding="utf-8")
print(f"_toc.yml updated with {len(recipes)} recipes.")