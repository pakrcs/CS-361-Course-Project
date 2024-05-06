# stats.py

import tkinter as tk
from tkinter import ttk

class StatsPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.club_entries = {}  # Dictionary to store club entry fields
        self.club_averages = {}  # Dictionary to store club average distances

        self.stats_label = tk.Label(self, text="Stats Page")
        self.stats_label.pack()

        self.initialize_averages()  # Initialize club averages dictionary

        # Create a notebook for club tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Add tabs for each club
        clubs = ["Driver", "3 Wood", "5 Wood", "2 Iron", "3 Iron", "4 Iron", "5 Iron", "6 Iron",
                 "7 Iron", "8 Iron", "9 Iron", "Pitching Wedge", "Gap Wedge", "52° Wedge",
                 "56° Wedge", "60° Wedge"]
        for club in clubs:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=club)
            self.add_club_distance_widgets(frame, club)

        self.back_button = tk.Button(self, text="Back to Main", command=self.back_to_main)
        self.back_button.pack()

    def add_club_distance_widgets(self, frame, club):
        club_label = tk.Label(frame, text=f"{club} Distance:")
        club_label.pack()

        club_entry = tk.Entry(frame)
        club_entry.pack()

        # Save the entry field in a dictionary for later access
        self.club_entries[club] = club_entry

        club_average_label = tk.Label(frame, text=f"{club} Average Distance:")
        club_average_label.pack()

        club_average_display = tk.Label(frame, textvariable=self.club_averages[club])
        club_average_display.pack()

    def calculate_averages(self):
        # Calculate average distance for each club
        for club, entry in self.club_entries.items():
            distances = entry.get().split(",")
            distances = [float(dist) for dist in distances if dist]  # Convert to floats and filter empty strings
            if distances:
                average_distance = sum(distances) / len(distances)
                self.club_averages[club].set(f"{club} Average Distance: {average_distance:.2f} yards")
            else:
                self.club_averages[club].set(f"No data for {club}")

    def back_to_main(self):
        self.pack_forget()  # Hide the current page
        self.master.main_screen.pack(fill=tk.BOTH, expand=True)  # Show the main screen again

    def initialize_averages(self):
        # Initialize club averages as StringVars
        self.notebook = ttk.Notebook(self)
        for club in ["Driver", "3 Wood", "5 Wood", "2 Iron", "3 Iron", "4 Iron", "5 Iron", "6 Iron",
                     "7 Iron", "8 Iron", "9 Iron", "Pitching Wedge", "Gap Wedge", "52° Wedge",
                     "56° Wedge", "60° Wedge"]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=club)
            self.club_averages[club] = tk.StringVar()
            self.club_averages[club].set(f"{club} Average Distance: N/A")
