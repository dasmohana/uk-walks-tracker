# UK Walks Tracker

Track and visualize your walking adventures across the UK with an interactive map.

This Python tool transforms your GPX files into a beautiful interactive map, allowing you to log and organize walks by region.

## Features

- Automatically detects new GPX files and updates `data/walks.yaml`.  
- Generates interactive **Folium maps** showing walked sections with folder-based color coding.  
- Supports journaling for each walk in Markdown (`docs/journals/`).  
- Assigns custom colors to each walk folder for easy identification.  
- Sidebar TOC shows all walks.

## Quick Start

### First Time Setup

1. **Fork this repo**

2. **Run the setup script** to create a virtual environment and install dependencies:

   **Windows:**
   ```bash
   setup.bat
   ```

   **Mac/Linux:**
   ```bash
   chmod +x setup.sh build.sh
   ./setup.sh
   ```

3. **Add your GPX files** to the `gpx` folder following the naming convention:

   `[start]-to-[destination].gpx`
   
   Example: `south-queensferry-to-boness.gpx`

### Building Your Documentation

**Single Command Build** - runs everything automatically:

**Windows:**
```bash
build.bat
```

**Mac/Linux:**
```bash
./build.sh
```

This will:
1. ✅ Update `walks.yaml` with new GPX files
2. ✅ Generate the interactive map
3. ✅ Create missing journal files
4. ✅ Build the Sphinx documentation

Your documentation will be ready at `docs/_build/html/index.html`

## Manual Steps (Advanced)

If you prefer to run steps individually:

1. **Update walks and generate map:**

    ```bash
    python scripts/update_uk_walks.py
    ```

    - New GPX files will automatically be added to `data/walks.yaml`
    - Folder colors are assigned and saved to `data/folder_colors.yaml`
    - The interactive map is generated at `docs/_static/map/index.html`
    - Missing journal files are auto-created

    > ⚠️ **Note:** If you delete a GPX file, you must manually remove the entry from `walks.yaml`.

2. **Build the Sphinx documentation:**

    ```bash
    cd docs
    make html          # Mac/Linux
    make.bat html      # Windows
    ```

## Project Structure

- **`gpx/`** - Your GPX track files organized by folder (e.g., `john-muir-way/`, `fife-coast-path/`)
- **`docs/journals/`** - Markdown journal files for each walk
- **`docs/_static/map/`** - Generated interactive map
- **`data/walks.yaml`** - Auto-generated walk metadata
- **`data/folder_colors.yaml`** - Color assignments for each walk folder

## Output

- Interactive map: `docs/_static/map/index.html`  
- Built documentation: `docs/_build/html/index.html`
- Journals: `docs/journals/`  
- Distance data: `data/distance.json`  

See the live site: [UK Walks Tracker](https://twotogether.github.io/uk-walks-tracker/)