import customtkinter as ctk

class HistoryPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        ctk.CTkLabel(self, text="Training History", font=("Roboto", 24, "bold")).pack(pady=20)
        
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=600, height=400, corner_radius=10)
        self.scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        sessions = [
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent"),
            ("14.06.2026", "45 min", "Excellent")
        ]
        
        for date, duration, score in sessions:
            card = ctk.CTkFrame(self.scroll_frame, fg_color="#2b2b3b", corner_radius=10)
            card.pack(fill="x", pady=5, padx=5)
            ctk.CTkLabel(card, text=f"{date} | {duration} | Score: {score}", 
                         font=("Roboto", 14)).pack(pady=10, padx=15)