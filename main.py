import customtkinter as ctk
from organizer import organize_folder
from config import DEFAULT_FOLDER
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organizador Inteligente")
        self.geometry("500x300")

        self.folder_path = ctk.StringVar(value=DEFAULT_FOLDER)

        self.label = ctk.CTkLabel(self, text="Pasta:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, textvariable=self.folder_path, width=350)
        self.entry.pack()

        self.button_browse = ctk.CTkButton(self, text="Selecionar Pasta", command=self.browse_folder)
        self.button_browse.pack(pady=10)

        self.button_organize = ctk.CTkButton(self, text="Organizar", command=self.run_organizer)
        self.button_organize.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def run_organizer(self):
        result = organize_folder(self.folder_path.get())
        self.result_label.configure(text=result)

if __name__ == "__main__":
    app = App()
    app.mainloop()