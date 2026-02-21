from pathlib import Path
import shutil
import hashlib

CATEGORIES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Compactados": [".zip", ".rar", ".7z"],
}

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def organize_folder(folder_path, progress_callback=None, log_callback=None):
    folder = Path(folder_path)

    if not folder.exists():
        return

    files = [f for f in folder.iterdir() if f.is_file()]
    total = len(files)
    moved = 0

    for i, file in enumerate(files):
        for category, extensions in CATEGORIES.items():
            if file.suffix.lower() in extensions:
                category_folder = folder / category
                category_folder.mkdir(exist_ok=True)

                shutil.move(str(file), str(category_folder / file.name))
                moved += 1

                if log_callback:
                    log_callback(f"Movido: {file.name} → {category}")

                break

        if progress_callback:
            progress_callback((i + 1) / total)

def rename_files(folder_path, log_callback=None):
    folder = Path(folder_path)

    for file in folder.rglob("*"):
        if file.is_file():
            new_name = file.stem.replace(" ", "_") + file.suffix
            new_path = file.with_name(new_name)

            if file != new_path:
                file.rename(new_path)

                if log_callback:
                    log_callback(f"Renomeado: {file.name} → {new_name}")

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

def remove_duplicates(folder_path, log_callback=None):
    duplicates = find_duplicates(folder_path)

    for file in duplicates:
        if log_callback:
            log_callback(f"Duplicado removido: {file.name}")

        file.unlink()

    return len(duplicates)