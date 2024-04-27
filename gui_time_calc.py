import tkinter as tk
from tkinter import ttk
from time_calc import add_time

def calculate_time():
    start_time = start_entry.get()
    add_time_str = add_entry.get()
    day = day_entry.get()

    result = add_time(start_time, add_time_str, day)
    result_label.config(text=result)

root = tk.Tk()
root.title("Time Calculator")

start_label = ttk.Label(root, text="Start Time (HH:MM AM/PM):")
start_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

add_label = ttk.Label(root, text="Time to Add (HH:MM):")
add_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

day_label = ttk.Label(root, text="Day (optional):")
day_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

start_entry = ttk.Entry(root, width=20)
start_entry.grid(row=0, column=1, padx=5, pady=5)

add_entry = ttk.Entry(root, width=20)
add_entry.grid(row=1, column=1, padx=5, pady=5)

day_entry = ttk.Entry(root, width=20)
day_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_time)
calculate_button.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
