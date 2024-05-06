import tkinter as tk
from user_profiles import UserProfilesPage
from stats import StatsPage

class GolfApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Golf Tracer App")

        self.main_screen = MainScreen(self)
        self.main_screen.pack(fill=tk.BOTH, expand=True)

        self.user_profiles_page = UserProfilesPage(self)
        self.stats_page = StatsPage(self)

    def show_user_profiles(self):
        self.main_screen.pack_forget()
        self.user_profiles_page.pack(fill=tk.BOTH, expand=True)

    def show_stats(self):
        self.main_screen.pack_forget()
        self.stats_page.pack(fill=tk.BOTH, expand=True)

class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_profiles_button = tk.Button(self, text="User Profile", command=master.show_user_profiles)
        self.user_profiles_button.pack()

        self.stats_button = tk.Button(self, text="My Stats", command=master.show_stats)
        self.stats_button.pack()

if __name__ == "__main__":
    app = GolfApp()
    app.mainloop()
