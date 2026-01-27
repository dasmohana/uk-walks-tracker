import sys
import yaml
import folium
import json
import gpxpy
from pathlib import Path
from geopy.distance import geodesic

# --- Setup paths ---
BASE_DIR = Path(__file__).resolve().parent.parent  # project root
GPX_DIR = BASE_DIR / "gpx"
WALKS_YAML = BASE_DIR / "data" / "walks.yaml"
DATA_DIR = BASE_DIR / "data"
FOLDER_COLORS_FILE = BASE_DIR / "data" / "folder_colors.yaml"
MAP_DIR = BASE_DIR / "docs" / "map"
JOURNALS_DIR = BASE_DIR / "docs" / "journals"

MAP_DIR.mkdir(parents=True, exist_ok=True)
JOURNALS_DIR.mkdir(parents=True, exist_ok=True)

# Make scripts importable
SCRIPTS_DIR = BASE_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
from create_journals import create_journals


# ---------------------------------
# Step 1 — Update walks.yaml
# ---------------------------------
def update_coastal_walks():
    """Scan all GPX subfolders and update walks.yaml."""
    if not GPX_DIR.exists():
        print(f"⚠️ GPX folder does not exist: {GPX_DIR}")
        return []

    with open(WALKS_YAML, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if "walks" not in data:
        data["walks"] = []

    existing_gpx = {walk["gpx"] for walk in data["walks"]}
    new_walks_added = []

    # Recursive GPX scan
    for gpx_file in GPX_DIR.rglob("*.gpx"):
        relative_path = gpx_file.relative_to(BASE_DIR).as_posix()

        if relative_path not in existing_gpx:
            name = gpx_file.stem.replace("-", " ").title()

            # Determine region folder based on GPX subfolder
            region_folder = gpx_file.relative_to(GPX_DIR).parent.as_posix()
            journal_md = f"journals/{region_folder}/{gpx_file.stem}.md"

            new_walk = {
                "name": name,
                "gpx": relative_path,
                "journal": journal_md,
            }

            data["walks"].append(new_walk)
            new_walks_added.append(new_walk)

    # Save updates
    if new_walks_added:
        with open(WALKS_YAML, "w", encoding="utf-8") as f:
            yaml.dump(data, f, sort_keys=False)
        print(f"✅ walks.yaml updated with {len(new_walks_added)} new GPX file(s).")
    else:
        print("ℹ️ No new GPX files found.")

    return new_walks_added


new_walks = update_coastal_walks()


# ---------------------------------
# Step 2 — Generate journals
# ---------------------------------
create_journals()


# ---------------------------------
# Step 3 — Load updated YAML and folder colors
# ---------------------------------
with open(WALKS_YAML, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

if FOLDER_COLORS_FILE.exists():
    with open(FOLDER_COLORS_FILE, "r", encoding="utf-8") as f:
        folder_colors = yaml.safe_load(f) or {}
else:
    folder_colors = {}


# ---------------------------------
# Step 4 — Initialize map
# ---------------------------------
m = folium.Map(location=[54.5, -3.0], zoom_start=6, tiles="OpenStreetMap")
SITE_ROOT = "https://twotogether.github.io/uk-walks-tracker"


# ---------------------------------
# Step 5 — Load GPX, add to map
# ---------------------------------
for walk in data.get("walks", []):
    name = walk["name"]
    coords = []

    gpx_path = BASE_DIR / walk["gpx"]

    if not gpx_path.exists():
        print(f"⚠️ Missing GPX file: {gpx_path}")
        continue

    # Parse GPX
    with open(gpx_path, "r", encoding="utf-8") as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        
        # Extract coordinates from tracks
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    coords.append([point.latitude, point.longitude])
        
        # Extract coordinates from routes (fallback if no tracks)
        for route in gpx.routes:
            for point in route.points:
                coords.append([point.latitude, point.longitude])

    if not coords:
        continue

    # Build journal URL (Sphinx builds .html versions)
    journal_html = walk["journal"].replace(".md", ".html")
    journal_url = f"{SITE_ROOT}/{journal_html}"

    popup_html = f"<b>{name}</b><br><a href='{journal_url}' target='_blank'>View Journal</a>"

    # Get color based on GPX subfolder
    gpx_rel_path = Path(walk["gpx"]).relative_to("gpx")
    folder_name = gpx_rel_path.parts[0]
    color = folder_colors.get(folder_name, "#808080")  # Default to gray if folder not in mapping

    folium.PolyLine(coords, color=color, weight=4, popup=popup_html).add_to(m)

    print(f"✅ Added: {name}")


# ---------------------------------
# Step 7 — Save Map
# ---------------------------------
map_out = MAP_DIR / "index.html"
m.save(map_out)
print(f"\n✅ Map saved to {map_out}")


# ---------------------------------
# Summary
# ---------------------------------
if new_walks:
    print("\n🆕 Newly added GPX files:")
    for w in new_walks:
        print(f" - {w['gpx']}")
