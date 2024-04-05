import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = ttk.Frame(root)


def increment():
    progressBar.step(20)


def decrement():
    progressBar.step(-20)


def display():
    print(progressBar["value"])


progressBar = ttk.Progressbar(frame, mode='determinate')
progressBar.pack(padx=10, pady=10)

button = ttk.Button(frame, text="Increment-20", command=increment)
button.pack(padx=10, pady=10, side=tk.LEFT)

button = ttk.Button(frame, text="Decrement-20", command=decrement)
button.pack(padx=10, pady=10, side=tk.LEFT)
button = ttk.Button(frame, text="Show-Result", command=display)
button.pack(padx=10, pady=10, side=tk.LEFT)

frame.pack(padx=5, pady=5)
root.mainloop()