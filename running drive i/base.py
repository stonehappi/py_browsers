import os
import shutil
from pathlib import Path


def move_file(file, new_file) -> None:
    folder = "/".join(new_file.split("/")[:-1])
    Path(folder).mkdir(parents=True, exist_ok=True)
    shutil.move(file, new_file)


def delete_empty_folders(path) -> None:
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except:
                pass
