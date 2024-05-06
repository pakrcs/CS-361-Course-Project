# stats.py

import tkinter as tk
from tkinter import ttk

class StatsPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.club_averages = {}  # Dictionary to store club average distances
        self.club_distance_entries = {}  # Dictionary to store club distance entry widgets
        self.club_tables = {}  # Dictionary to store club tables
        self.average_labels = {}  # Dictionary to store labels for average distances

        self.stats_label = tk.Label(self, text="Stats Page")
        self.stats_label.pack()

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
            self.create_club_table(frame, club)

        self.back_button = tk.Button(self, text="Back to Main", command=self.back_to_main)
        self.back_button.pack()

    def create_club_table(self, frame, club):
        # Table to display submitted distances for each club
        table = ttk.Treeview(frame, columns=["Distance"], show="headings")
        table.heading("Distance", text="Distance")
        table.pack()

        input_frame = ttk.Frame(frame)
        input_frame.pack()

        distance_label = tk.Label(input_frame, text=f"{club} Distance:")
        distance_label.pack(side=tk.LEFT)

        distance_entry = tk.Entry(input_frame)
        distance_entry.pack(side=tk.LEFT)

        # Store the distance entry widget in the dictionary for later access
        self.club_distance_entries[club] = distance_entry
        self.club_tables[club] = table

        submit_button = tk.Button(input_frame, text="Submit Distance", command=lambda entry=distance_entry, tbl=table, clb=club: self.submit_distance(entry, tbl, clb))
        submit_button.pack(side=tk.LEFT)

        # Label to display average distance dynamically
        average_label = tk.Label(frame, text="")
        average_label.pack()
        self.average_labels[club] = average_label

    def submit_distance(self, entry, table, club):
        # Get distance from user input and add it to the table
        distance = entry.get()
        if distance:
            table.insert("", "end", values=(distance,))
            entry.delete(0, tk.END)  # Clear the entry after submission

            # Calculate average distance for the club
            total_distance = 0
            count = 0
            for item in table.get_children():
                total_distance += float(table.item(item)["values"][0])
                count += 1
            if count > 0:
                average_distance = total_distance / count
                self.club_averages[club] = f"{club} Average Distance: {average_distance:.2f} yards"
                self.average_labels[club].config(text=self.club_averages[club])  # Update average label dynamically

    def back_to_main(self):
        self.pack_forget()  # Hide the current page
        self.master.main_screen.pack(fill=tk.BOTH, expand=True)  # Show the main screen again
