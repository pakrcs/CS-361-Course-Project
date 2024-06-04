import tkinter as tk
from tkinter import messagebox, ttk
import random
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

    def send_feedback(self, website_owner_email, user_email, feedback, feedback_rating):
        url = 'https://email-server-smoky.vercel.app/emailServer'
        headers = {'Content-Type': 'application/json'}
        data = {
            'websiteOwnerEmail': website_owner_email,
            'userEmail': user_email,
            'feedback': feedback,
            'feedbackRating': feedback_rating
        }
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            messagebox.showinfo("Feedback Sent", "Thank you for your feedback!")
        else:
            messagebox.showerror("Error", "Failed to send feedback.")

    def compare_with_tour_averages(self):
        def compare():
            try:
                distance = float(distance_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid distance.")
                return

            tour_averages_url = f'http://localhost:5004/compare_distance?distance={distance}'
            tour_averages_response = requests.get(tour_averages_url)
            
            if tour_averages_response.status_code == 200:
                tour_averages_data = tour_averages_response.json()
                comparison_label.config(text="Comparison with Tour Averages:")
                for club, difference in tour_averages_data.items():
                    comparison_label.config(text=f"{comparison_label.cget('text')}\n{club}: {difference:.1f} yards")
            else:
                messagebox.showerror("Error", "Failed to fetch tour averages data.")

        comparison_window = tk.Toplevel(self)
        comparison_window.title("Compare with Tour Averages")

        tk.Label(comparison_window, text="Enter your distance:").pack()
        distance_entry = tk.Entry(comparison_window)
        distance_entry.pack()

        tk.Button(comparison_window, text="Compare", command=compare).pack()
        comparison_label = tk.Label(comparison_window, text="")
        comparison_label.pack()

    def send_goal(self, goal_text):
        url = 'http://localhost:5005/submit_goal'
        data = {'goal': goal_text}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return True
        else:
            messagebox.showerror("Error", "Failed to submit goal.")
            return False
        
    def generate_random_goal(self):
        try:
            with open('golf_goals.txt', 'r') as file:
                goals_list = file.readlines()
            random_goal = random.choice(goals_list).strip()
            self.main_screen.display_random_goal(random_goal)
        except FileNotFoundError:
            messagebox.showerror("Error", "golf_goals.txt not found.")


class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_profiles_button = tk.Button(self, text="User Profile", command=master.show_user_profiles)
        self.user_profiles_button.pack()

        self.stats_button = tk.Button(self, text="My Stats", command=master.show_stats)
        self.stats_button.pack()

        self.club_recommendation_button = tk.Button(self, text="Club Recommendation", command=master.show_club_recommendation)
        self.club_recommendation_button.pack()

        self.compare_button = tk.Button(self, text="Compare with Tour Averages", command=master.compare_with_tour_averages)
        self.compare_button.pack()

        self.courses_button = tk.Button(self, text="Golf Courses", command=self.show_courses_window)
        self.courses_button.pack()

        self.golf_goals_button = tk.Button(self, text="Golf Goals", command=self.open_goals_window)
        self.golf_goals_button.pack()

        self.quotes_button = tk.Button(self, text="Quotes", command=master.show_quotes)
        self.quotes_button.pack()

        self.feedback_button = tk.Button(self, text="Feedback", command=self.show_feedback_window)
        self.feedback_button.pack()

    def show_feedback_window(self):
        feedback_window = tk.Toplevel(self)
        feedback_window.title("Feedback")

        tk.Label(feedback_window, text="Website Owner Email:").pack()
        website_owner_entry = tk.Entry(feedback_window)
        website_owner_entry.pack()

        tk.Label(feedback_window, text="User Email:").pack()
        user_email_entry = tk.Entry(feedback_window)
        user_email_entry.pack()

        tk.Label(feedback_window, text="Feedback:").pack()
        feedback_entry = tk.Entry(feedback_window)
        feedback_entry.pack()

        tk.Label(feedback_window, text="Feedback Rating (0-5):").pack()
        feedback_rating_entry = tk.Entry(feedback_window)
        feedback_rating_entry.pack()

        send_feedback_button = tk.Button(feedback_window, text="Send Feedback", command=lambda: self.master.send_feedback(
            website_owner_entry.get(),
            user_email_entry.get(),
            feedback_entry.get(),
            feedback_rating_entry.get()
        ))
        send_feedback_button.pack()

    def open_goals_window(self):
        goals_window = tk.Toplevel(self)
        goals_window.title("Golf Goals")

        self.goal_label = tk.Label(goals_window, text="Enter Your Golf Goal:")
        self.goal_label.pack()

        self.goal_entry = tk.Entry(goals_window)
        self.goal_entry.pack()

        self.submit_goal_button = tk.Button(goals_window, text="Submit Goal", command=self.submit_goal)
        self.submit_goal_button.pack()

        self.generate_goal_button = tk.Button(goals_window, text="Generate a Goal", command=self.generate_random_goal)
        self.generate_goal_button.pack()

        self.submitted_goal_label = tk.Label(goals_window, text="")
        self.submitted_goal_label.pack()

    def submit_goal(self):
        goal_text = self.goal_entry.get()
        if goal_text:
            success = self.master.send_goal(goal_text)
            if success:
                self.submitted_goal_label.config(text=f"Submitted Goal:\n{goal_text}")
                self.goal_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid goal.")

    def generate_random_goal(self):
        try:
            with open('golf_goals.txt', 'r') as file:
                goals_list = file.readlines()
            random_goal = random.choice(goals_list).strip()
            self.submitted_goal_label.config(text=f"Generated Goal:\n{random_goal}")
        except FileNotFoundError:
            messagebox.showerror("Error", "golf_goals.txt not found.")

    def show_courses_window(self):
        courses_window = tk.Toplevel(self)
        courses_window.title("Golf Courses")

        for course in self.fetch_courses_data():
            tk.Label(courses_window, text=f"Name: {course['name']}").pack()
            tk.Label(courses_window, text=f"Location: {course['location']}").pack()
            tk.Label(courses_window, text=f"Par: {course['par']}").pack()
            tk.Label(courses_window, text=f"Rating: {course['rating']}").pack()
            tk.Label(courses_window, text=f"Description: {course['description']}").pack()
            tk.Label(courses_window, text="------------------------").pack()

    def fetch_courses_data(self):
        try:
            response = requests.get('http://localhost:5006/get_courses')
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", "Failed to fetch course data.")
                return []
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Request Error: {e}")
            return []


if __name__ == "__main__":
    app = GolfApp()
    app.mainloop()
