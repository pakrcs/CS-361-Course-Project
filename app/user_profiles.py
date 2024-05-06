import tkinter as tk

class UserProfilesPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_label = tk.Label(self, text="User Profile")
        self.user_label.pack()

        self.back_button = tk.Button(self, text="Back to Main Menu", command=self.back_to_main)
        self.back_button.pack()

    def back_to_main(self):
        self.pack_forget()  # Hide the current page
        self.master.main_screen.pack(fill=tk.BOTH, expand=True)  # Show the main screen again
