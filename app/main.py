import tkinter as tk
from user_profiles import UserProfilesPage
from stats import StatsPage
import requests  # Import requests for HTTP communication


class GolfApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Golf Tracker App")

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

    def get_inspirational_quote(self):
        response = requests.get('http://localhost:5002/get_quote')
        if response.status_code == 200:
            quote_data = response.json()
            inspirational_quote = quote_data['quote']
            tk.messagebox.showinfo("Quote of the Day", inspirational_quote)
        else:
            tk.messagebox.showerror("Error", "Failed to fetch quote.")


class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_profiles_button = tk.Button(self, text="User Profile", command=master.show_user_profiles)
        self.user_profiles_button.pack()

        self.stats_button = tk.Button(self, text="My Stats", command=master.show_stats)
        self.stats_button.pack()

        self.quotes_button = tk.Button(self, text="Quote of the Day", command=master.get_inspirational_quote)
        self.quotes_button.pack()


if __name__ == "__main__":
    app = GolfApp()
    app.mainloop()
