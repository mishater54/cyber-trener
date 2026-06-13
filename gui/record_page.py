import customtkinter as ctk

class RecordsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        ctk.CTkLabel(self, text="Personal Records", font=("Roboto", 24, "bold")).pack(pady=20)
        
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(padx=20, pady=20)
        
        records = [
            ("Longest Session", "1h 20m"),
            ("Highest Score", "98%"),
            ("Max Streak", "12 Days"),
            ("Modules Cleared", "42")
        ]
        
        for i, (title, value) in enumerate(records):
            row = i // 2
            col = i % 2
            
            card = ctk.CTkFrame(self.grid_frame, fg_color="#2b2b3b", corner_radius=15, width=400, height=160)
            card.grid(row=row, column=col, padx=25, pady=25, sticky="ew")
            card.grid_propagate(False)
            
            ctk.CTkLabel(card, text=title, font=("Roboto", 16), text_color="gray").pack(pady=(25, 5))
            ctk.CTkLabel(card, text=value, font=("Roboto", 28, "bold"), text_color="#00d4ff").pack()