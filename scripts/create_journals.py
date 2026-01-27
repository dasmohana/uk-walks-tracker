import json
from pathlib import Path

def create_journals():
    """
    Create missing Markdown journals for GPX files and update journals/index.json.
    Scans gpx/ folder, creates corresponding journals in docs/journals/ with folder structure.
    """
    BASE_DIR = Path(__file__).resolve().parent.parent
    GPX_DIR = BASE_DIR / "gpx"
    JOURNALS_DIR = BASE_DIR / "docs" / "journals"
    JOURNALS_DIR.mkdir(parents=True, exist_ok=True)

    new_files = []

    # Find all .gpx files
    if GPX_DIR.exists():
        for gpx_file in GPX_DIR.rglob("*.gpx"):
            # Get the relative path structure from GPX_DIR
            rel_path = gpx_file.relative_to(GPX_DIR)
            folder = rel_path.parent
            gpx_name = gpx_file.stem
            
            # Create corresponding journal path with same folder structure
            journal_folder = JOURNALS_DIR / folder
            journal_folder.mkdir(parents=True, exist_ok=True)
            journal_file = journal_folder / f"{gpx_name}.md"
            
            # Create journal if it doesn't exist
            if not journal_file.exists():
                title = gpx_name.replace('-', ' ').title()
                journal_file.write_text(
                    f"# {title}\n\n"
                    "## Walk Metadata\n\n"
                    "| Attribute | Value |\n"
                    "| --------- | ----- |\n"
                    "| **Difficulty** | |\n"
                    "| **Distance** | |\n"
                    "| **Duration** | |\n"
                    "| **Elevation Gain** | |\n"
                    "| **Terrain** | |\n"
                    "| **Accessibility** | |\n"
                    "| **Can be done by public transport** | |\n\n"
                    "## Getting There\n\n"
                    "**Start:**\n"
                    "- **Train**: \n"
                    "- **Bus**: \n"
                    "- **Parking**: \n\n"
                    "**End:**\n"
                    "- **Train**: \n"
                    "- **Bus**: \n"
                    "- **Parking**: \n\n"
                    "## Route\n\n"
                    "| Section Walked  | Distance | Date |\n"
                    "| --------------- | -------- | ---- |\n\n"
                    "## Description\n\n"
                    "Add walk description here.\n\n"
                    "## Notes\n\n"
                    "- Add notes, photos, and links here.\n",
                    encoding="utf-8"
                )
                rel_path_str = rel_path.as_posix()
                new_files.append(rel_path_str)

    # Recursively find all existing .md files inside docs/journals/
    md_files = sorted([f.relative_to(JOURNALS_DIR).as_posix() for f in JOURNALS_DIR.rglob("*.md")])

    # Update index.json
    with open(JOURNALS_DIR / "index.json", "w", encoding="utf-8") as f:
        json.dump(md_files, f, indent=2)

    print(f"📁 journals/index.json updated with {len(md_files)} entries.")
    if new_files:
        print(f"📝 Created {len(new_files)} new journal(s):\n  " + "\n  ".join(new_files))
    else:
        print("✓ All GPX files have corresponding journals.")

if __name__ == "__main__":
    create_journals()
