# UK Coastal Walk Tracker

A Python project to track and visualise coastal walks around the UK.

This tool allows you to log GPX walks, generate a map of the coastline you’ve walked, calculate distances, and see your progress as a fraction of the total UK coastline.

## Features

- Automatically detects new GPX files and updates `data/walks.yaml`.  
- Generates interactive **Folium maps** showing walked sections with folder-based color coding.  
- Calculates total distance walked and fraction of UK coastline completed.  
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

See [UK coast walk tracker](https://twotogether.github.io/uk-coast-walk-tracker/index.html).