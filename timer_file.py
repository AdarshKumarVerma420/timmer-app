import tkinter as tk
from tkinter import messagebox
import time
import threading

def run_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"Time Remaining: {mins:02d}:{secs:02d}")
        root.update()
        time.sleep(1)
        seconds -= 1
    if seconds == 0:
        timer_label.config(text="Time Remaining: 00:00")
        messagebox.showinfo("Timer", "Time's up!")

def start_timer():
    try:
        minutes = int(entry.get())
        threading.Thread(target=run_timer, args=(minutes,)).start()  # Run timer in a new thread
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

root = tk.Tk()
root.title("Timer App")


entry_label = tk.Label(root, text="Set timer in minutes:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# Button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

# Label to show remaining time
timer_label = tk.Label(root, text="Time Remaining: 00:00", font=("Helvetica", 18))
timer_label.pack()

# Run the tkinter loop
root.mainloop()
