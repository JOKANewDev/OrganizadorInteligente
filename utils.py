import hashlib
from pathlib import Path

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(folder_path):
    folder = Path(folder_path)
    hashes = {}
    duplicates = []

    for file in folder.rglob("*"):
        if file.is_file():
            file_hash = get_file_hash(file)
            if file_hash in hashes:
                duplicates.append(file)
            else:
                hashes[file_hash] = file

    return duplicates