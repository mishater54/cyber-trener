import customtkinter as ctk

class StatsPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        ctk.CTkLabel(self, text="Performance Stats", font=("Roboto", 24, "bold")).pack(pady=20)
        
        self.content_frame = ctk.CTkFrame(self, fg_color="#2b2b3b", corner_radius=15)
        self.content_frame.pack(padx=40, pady=20, fill="both", expand=True)
        
        stats = [
            ("Total Sessions:", "142"),
            ("Average Accuracy:", "91%"),
            ("Training Time This Week:", "5h 45m")
        ]
        
        for label, value in stats:
            row_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
            row_frame.pack(fill="x", padx=40, pady=20)
            
            ctk.CTkLabel(row_frame, text=label, font=("Roboto", 18)).pack(side="left")
            ctk.CTkLabel(row_frame, text=value, font=("Roboto", 18, "bold"), text_color="#00d4ff").pack(side="right")
        
        # Weekly Goal Progress Bar
        ctk.CTkLabel(self.content_frame, text="Weekly Goal Progress (8h)", font=("Roboto", 16)).pack(pady=(40, 10))
        
        self.progress = ctk.CTkProgressBar(self.content_frame, width=400, height=15, progress_color="#00d4ff")
        self.progress.pack(pady=10)
        self.progress.set(0.7)