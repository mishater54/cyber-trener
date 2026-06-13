import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        self.video_label = ctk.CTkLabel(self, text="[ Live Feed: Awaiting Input ]", font=("Roboto", 18))
        self.video_label.pack(expand=True)
        
        self.start_btn = ctk.CTkButton(self, text="Start new training", corner_radius=25, 
                                       height=50, font=("Roboto", 16, "bold"),
                                       fg_color="#00d4ff", text_color="black")
        self.start_btn.pack(pady=20, padx=40, fill="x")