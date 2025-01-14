import pandas as pd

from base import move_file, delete_empty_folders


def run_drive_h():
    df = pd.read_csv("files/drive_h.csv")
    df_target = df[df["target"].notnull()]
    for index, row in df_target.iterrows():
        old_path = (
            row["file_path"]
            .replace("\\", "/")
            .replace("D:/E-Library Docs/Backup Plush (H)", "data/h")
        )
        new_path = row["path"].replace("\\", "/").replace("h_clean", "data/e")
        try:
            move_file(old_path, new_path)
        except Exception as e:
            print(f"Error: {e}")
            continue


def main():
    # run_drive_h()
    delete_empty_folders("data/h")

main()