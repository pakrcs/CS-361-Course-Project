import tkinter as tk
from tkinter import messagebox


class CreateProfileWindow(tk.Toplevel):
    """Window for users to enter profile information when creating a new profile."""

    def __init__(self, master, user_profiles_page):
        super().__init__(master)

        self.title("Create Profile")
        self.user_profiles_page = user_profiles_page

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, sticky=tk.E)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=1, column=0, sticky=tk.E)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1)

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.grid(row=2, column=0, sticky=tk.E)

        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=2, column=1)

        self.handicap_label = tk.Label(self, text="Handicap:")
        self.handicap_label.grid(row=3, column=0, sticky=tk.E)

        self.handicap_entry = tk.Entry(self)
        self.handicap_entry.grid(row=3, column=1)

        self.years_playing_label = tk.Label(self, text="Years Playing:")
        self.years_playing_label.grid(row=4, column=0, sticky=tk.E)

        self.years_playing_entry = tk.Entry(self)
        self.years_playing_entry.grid(row=4, column=1)

        self.create_button = tk.Button(self, text="Create", command=self.create_profile)
        self.create_button.grid(row=5, columnspan=2)

    def create_profile(self):
        # User inputs data into entry fields
        username = self.username_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        handicap = self.handicap_entry.get()
        years_playing = self.years_playing_entry.get()

        # Validate input (add your validation logic here)
        if not username or not name or not age or not handicap or not years_playing:
            messagebox.showwarning("Error", "Please fill in all fields.")
            return

        # Send the profile data back to the UserProfilesPage
        profile_data = {
            "Username": username,
            "Name": name,
            "Age": age,
            "Handicap": handicap,
            "Years Playing": years_playing
        }
        self.user_profiles_page.update_profile(profile_data)
        self.destroy()


class UserProfilesPage(tk.Frame):
    """Page for users to enter information and preferences for the application."""

    def __init__(self, master):
        super().__init__(master)
        # Create dictionary to store user data
        self.profile_data = {}

        self.user_label_frame = tk.Frame(self)
        self.user_label_frame.pack()

        self.user_label = tk.Label(self.user_label_frame, text="User Profile")
        self.user_label.pack(side=tk.LEFT)

        self.info_button = tk.Button(self.user_label_frame, text="(i)", command=self.show_description)
        self.info_button.pack(side=tk.LEFT)

        self.create_profile_button = tk.Button(self, text="Create Profile", command=self.create_profile_window)
        self.create_profile_button.pack()

        self.profile_display_label = tk.Label(self, text="")
        self.profile_display_label.pack()

        self.back_button = tk.Button(self, text="Back to Main", command=self.back_to_main)
        self.back_button.pack(side=tk.BOTTOM)

    def show_description(self):
        # IH2 tells the user why it would useful to set up a profile
        description = ("Creating a profile allows you to track your progress over time by "
                       "saving club distances. It also allows you the ability to "
                       "access club recommendations for certain scenarios. ")

        messagebox.showinfo("Information", description)

    def create_profile_window(self):
        # Open the profile creation window
        profile_window = CreateProfileWindow(self, self)

    def update_profile(self, profile_data):
        # Update the profile data and display it on the User Profile page
        self.profile_data = profile_data
        self.display_profile()

    def display_profile(self):
        # Display the profile data on the User Profile page
        profile_text = "\n".join(f"{key}: {value}" for key, value in self.profile_data.items())
        self.profile_display_label.config(text=profile_text)

    def back_to_main(self):
        self.pack_forget()
        self.master.main_screen.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = UserProfilesPage(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
