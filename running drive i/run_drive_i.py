import pandas as pd

from base import move_file, delete_empty_folders


def run_drive_i():
    df = pd.read_csv("drive_i.csv")
    df_target = df[df["target"].notnull()]
    for index, row in df_target.iterrows():
        old_path = (
            row["file_path"].replace("\\", "/").replace("B:/Traaanscend I", "data/i")
        )
        new_path = row["path"].replace("\\", "/").replace("i_clean", "data/e")
        try:
            move_file(old_path, new_path)
        except Exception as e:
            print(f"Error: {e}")
            continue


def main():
    run_drive_i()
    delete_empty_folders("data/i")
