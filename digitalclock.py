import tkinter as tk
import time


def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


# Create the main window
window = tk.Tk()
window.geometry("700x200")

# Clock label
clock_label = tk.Label(window, font=(
    "Courier New", 80), bg="black", fg="white")
clock_label.pack(pady=20)

# Window background and foreground color
window.configure(bg="midnight blue")
clock_label.configure(bg="midnight blue", fg="white")

# Font and size of the clock label
clock_label["font"] = ("Verdana", 80)

# Window title
window.title("My Digital Clock")

# Create a separator line
separator = tk.Frame(window, height=2, bd=2, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=20, pady=10)

# Creating a label for the date
date_label = tk.Label(window, font=("Arial", 16),
                      bg="midnight blue", fg="white")
date_label.pack(pady=10)

# Function to update the date


def update_date():
    current_date = time.strftime("%A, %B %d, %Y")
    date_label.config(text=current_date)
    # Update every minute (60,000 milliseconds)
    date_label.after(60000, update_date)


# Start updating the time and date
update_time()
update_date()

# Start the main event loop
window.mainloop()
