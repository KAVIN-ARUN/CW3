
import os
import shutil
import time

SRC_DIR = "src"
DATA_DIR = os.path.join(SRC_DIR, "data")
GENERATED_DIR = os.path.join(DATA_DIR, "generated")

WATCH_FILE = os.path.join("bib", "references.bib")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def copy_auxiliary_file(filename):
    src_file = os.path.join(DATA_DIR, filename)
    dst_file = os.path.join(GENERATED_DIR, filename)
    if os.path.exists(src_file):
        shutil.copyfile(src_file, dst_file)
        print(f"Copied {filename} to generated/")
    else:
        print(f"Warning: {filename} not found in data/")

def simulate_bib_to_js():
    # Minimal simulation
    bib_file = os.path.join(DATA_DIR, "generated", "bib.js")
    with open(bib_file, "w") as f:
        f.write("// Simulated bib.js")
    print("Simulated bib.js created.")

def update():
    print("Updating SurVis data...")
    ensure_dir(GENERATED_DIR)
    simulate_bib_to_js()
    copy_auxiliary_file("tag_categories.js")
    copy_auxiliary_file("authorized_tags.js")
    print("Update complete.")

def watch():
    print(f"Watching {WATCH_FILE} for changes...")
    last_modified = os.path.getmtime(WATCH_FILE)
    try:
        while True:
            time.sleep(2)
            current_modified = os.path.getmtime(WATCH_FILE)
            if current_modified != last_modified:
                update()
                last_modified = current_modified
    except KeyboardInterrupt:
        print("Stopped watching.")

if __name__ == "__main__":
    update()
    watch()
