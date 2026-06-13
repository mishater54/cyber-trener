import customtkinter as ctk

from home_page import HomePage
from history_page import HistoryPage

class CyberApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cyber Trainer")
        self.geometry("1000x600")

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=15)
        self.sidebar.pack(side="left", fill="y", padx=20, pady=20)

        ctk.CTkLabel(self.sidebar, text="Menu", font=("Roboto", 20, "bold")).pack(pady=20)
        
        ctk.CTkButton(self.sidebar, text="Home", command=lambda: self.switch_page("home"), corner_radius=20).pack(pady=10, padx=20, fill="x")
        ctk.CTkButton(self.sidebar, text="History", command=lambda: self.switch_page("history"), corner_radius=20).pack(pady=10, padx=20, fill="x")
        ctk.CTkButton(self.sidebar, text="Records", command=lambda: self.switch_page("records"), corner_radius=20).pack(pady=10, padx=20, fill="x")
        ctk.CTkButton(self.sidebar, text="Stats", command=lambda: self.switch_page("stats"), corner_radius=20).pack(pady=10, padx=20, fill="x")

        self.main_container = ctk.CTkFrame(self, corner_radius=15)
        self.main_container.pack(side="right", expand=True, fill="both", padx=20, pady=20)

        self.pages = {
            "home": HomePage(self.main_container),
            "history": HistoryPage(self.main_container)
        }
        
        self.switch_page("home")

    def switch_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = CyberApp()
    app.mainloop()