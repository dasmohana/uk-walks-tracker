# UK Walks Tracker

Track and visualize your walking adventures across the UK with an interactive map.

This Python tool transforms your GPX files into a beautiful interactive map, allowing you to log and organize walks by region.

## Features

- Automatically detects new GPX files and updates `data/walks.yaml`.  
- Generates interactive **Folium maps** showing walked sections with folder-based color coding.  
- Supports journaling for each walk in Markdown (`docs/journals/`).  
- Assigns custom colors to each walk folder for easy identification.  
- Sidebar TOC shows all walks.

## How to Use This

1. Fork this repo.

2. Place your GPX files in the `gpx` folder following the naming convention:

    `[start]-to-[destination].gpx`
    
    Example: `s-queensferry-to-boness.gpx`

3. Run the update script:

    ```bash
    python scripts/update_uk_walks.py
    ```

    - New GPX files will automatically be added to `data/walks.yaml`.  
    - Folder colors are assigned and saved to `data/folder_colors.yaml`.  
    - The interactive map is generated and saved in `docs/map/index.html`.

    > ⚠️ If you delete a GPX file, you must manually remove the entry from `walks.yaml`.

4. Generate journal Markdown files (optional, if not auto-generated):

    ```bash
    python scripts/create_journals.py
    ```

4. Build the Sphinx documentation:

    ```bash
    cd docs
    make html
    ```

    - The homepage shows the embedded map.  
    - Sidebar displays all walks organised by region.  

5. Verify the output locally by opening:

    ```bash
    open _build/html/index.html  # or navigate in your file browser
    ```

## Output

- Interactive map: `docs/map/index.html`  
- Journals: `docs/journals/`  
- Distance data: `data/distance.json`  

See [UK Walks Tracker](https://twotogether.github.io/uk-walks-tracker/).