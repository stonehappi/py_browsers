# remove all if that file is .DS_Store or desktop.ini or Thumbs.db
#
# Usage: python delete_usless.py
#

import os

def walk_dir(tdir):
    for root, dirs, files in os.walk(tdir):
        for file in files:
            if file == ".DS_Store" or file == "desktop.ini" or file == "Thumbs.db":
                os.remove(os.path.join(root, file))
                print(f"Removed {file} in {root}")

walk_dir("data/i")