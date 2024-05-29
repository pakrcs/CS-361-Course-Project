import tkinter as tk
from tkinter import messagebox, ttk
import requests
from user_profiles import UserProfilesPage
from stats import StatsPage


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

    def show_club_recommendation(self):
        self.get_club_recommendation()

    def get_club_recommendation(self):
        def recommend():
            try:
                distance = float(distance_entry.get())
                wind_condition = wind_combobox.get()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid distance.")
                return

            response = requests.get(f'http://localhost:5003/recommend_club?distance={distance}&wind_condition={wind_condition}')
            if response.status_code == 200:
                recommendation_data = response.json()
                recommended_club = recommendation_data.get('recommended_club', 'Error')
                recommendation_label.config(text=f"Recommended Club: {recommended_club}")
            else:
                messagebox.showerror("Error", "Failed to fetch club recommendation.")

        recommendation_window = tk.Toplevel(self)
        recommendation_window.title("Club Recommendation")

        tk.Label(recommendation_window, text="Distance to Hole:").pack()
        distance_entry = tk.Entry(recommendation_window)
        distance_entry.pack()

        tk.Label(recommendation_window, text="Wind Condition:").pack()
        wind_combobox = ttk.Combobox(recommendation_window, values=["None", "Downwind", "Into the Wind"])
        wind_combobox.pack()
        wind_combobox.set("None")

        tk.Button(recommendation_window, text="Get Recommendation", command=recommend).pack()
        recommendation_label = tk.Label(recommendation_window, text="")
        recommendation_label.pack()

    def show_quotes(self):
        self.get_inspirational_quote()

    def get_inspirational_quote(self):
        response = requests.get('http://localhost:5002/get_quote')
        if response.status_code == 200:
            quote_data = response.json()
            inspirational_quote = quote_data['quote']
            messagebox.showinfo("Inspirational Quote", inspirational_quote)
        else:
            messagebox.showerror("Error", "Failed to fetch quote.")


class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_profiles_button = tk.Button(self, text="User Profile", command=master.show_user_profiles)
        self.user_profiles_button.pack()

        self.stats_button = tk.Button(self, text="My Stats", command=master.show_stats)
        self.stats_button.pack()

        self.club_recommendation_button = tk.Button(self, text="Club Recommendation", command=master.show_club_recommendation)
        self.club_recommendation_button.pack()

        self.quotes_button = tk.Button(self, text="Quotes", command=master.show_quotes)
        self.quotes_button.pack()


if __name__ == "__main__":
    app = GolfApp()
    app.mainloop()
