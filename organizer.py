from pathlib import Path
import shutil

# Categorias por extensão
CATEGORIES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Compactados": [".zip", ".rar", ".7z"],
}

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        return "Pasta não encontrada."

    moved_files = 0

    for file in folder.iterdir():
        if file.is_file():
            for category, extensions in CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    category_folder = folder / category
                    category_folder.mkdir(exist_ok=True)

                    shutil.move(str(file), str(category_folder / file.name))
                    moved_files += 1
                    break

    return f"{moved_files} arquivos organizados."