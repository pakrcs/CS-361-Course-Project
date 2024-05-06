import tkinter as tk

class StatsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.stats_label = tk.Label(self, text="My Stats")
        self.stats_label.pack()

        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.back_to_main)
        self.back_button.pack()

    def back_to_main(self):
        self.pack_forget()  # Hide the current page
        self.master.main_screen.pack(fill=tk.BOTH, expand=True)  # Show the main screen again
