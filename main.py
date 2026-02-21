import customtkinter as ctk
from tkinter import filedialog
from organizer import organize_folder, rename_files, remove_duplicates

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organizador Inteligente V2")
        self.geometry("600x500")

        self.folder_path = ctk.StringVar()

        ctk.CTkLabel(self, text="Pasta:").pack(pady=5)

        self.entry = ctk.CTkEntry(self, textvariable=self.folder_path, width=400)
        self.entry.pack()

        ctk.CTkButton(self, text="Selecionar Pasta", command=self.browse).pack(pady=5)
        ctk.CTkButton(self, text="Organizar", command=self.organize).pack(pady=5)
        ctk.CTkButton(self, text="Renomear Arquivos", command=self.rename).pack(pady=5)
        ctk.CTkButton(self, text="Remover Duplicados", command=self.remove_dupes).pack(pady=5)

        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.pack(pady=10)
        self.progress.set(0)

        ctk.CTkLabel(self, text="Log:").pack()

        self.log_box = ctk.CTkTextbox(self, width=500, height=200)
        self.log_box.pack(pady=5)

    def browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def log(self, message):
        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")

    def update_progress(self, value):
        self.progress.set(value)
        self.update_idletasks()

    def organize(self):
        self.progress.set(0)
        organize_folder(
            self.folder_path.get(),
            progress_callback=self.update_progress,
            log_callback=self.log
        )
        self.log("✔ Organização concluída\n")

    def rename(self):
        rename_files(self.folder_path.get(), log_callback=self.log)
        self.log("✔ Renomeação concluída\n")

    def remove_dupes(self):
        count = remove_duplicates(self.folder_path.get(), log_callback=self.log)
        self.log(f"✔ {count} duplicados removidos\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()