import os


def get_version(version_file_path: str) -> str:
    if not os.path.exists(version_file_path):
        return ""

    with open(version_file_path, "r", encoding="utf-8") as infile:
        return infile.read().strip()
