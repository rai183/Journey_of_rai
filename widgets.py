import tkinter as tk
from tkinter import ttk, messagebox

def show_message():
    messagebox.showinfo("Action", f"Hello, {entry.get()}!")

# 1. Initialize the Main Window
root = tk.Tk()
root.title("Tkinter Widget Gallery")
root.geometry("400x600")

# --- DISPLAY WIDGETS ---
tk.Label(root, text="--- Display Widgets ---", fg="grey").pack(pady=5)

# Label: Static text
label = tk.Label(root, text="I am a Label", font=("Arial", 12, "bold"))
label.pack()

# Message: Multi-line static text
msg = tk.Message(root, text="I am a Message widget. I wrap text automatically if the string is too long.", width=200)
msg.pack()

# --- INPUT WIDGETS ---
tk.Label(root, text="--- Input Widgets ---", fg="grey").pack(pady=5)

# Entry: Single-line input
entry = tk.Entry(root)
entry.insert(0, "Type your name here...")
entry.pack(pady=5)

# Button: Triggers a function
button = tk.Button(root, text="Click Me (Button)", command=show_message)
button.pack(pady=5)

# --- SELECTION WIDGETS ---
tk.Label(root, text="--- Selection Widgets ---", fg="grey").pack(pady=5)

# Checkbutton: Multiple choices
check_var = tk.IntVar()
check = tk.Checkbutton(root, text="Checkbutton (Toggle)", variable=check_var)
check.pack()

# Radiobuttons: Only one can be selected
radio_var = tk.StringVar(value="Option 1")
tk.Radiobutton(root, text="Radio A", variable=radio_var, value="A").pack()
tk.Radiobutton(root, text="Radio B", variable=radio_var, value="B").pack()

# Scale: A slider for numbers
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Scale (Slider)")
scale.pack(pady=5)

# --- ORGANIZATIONAL WIDGETS ---
tk.Label(root, text="--- Containers ---", fg="grey").pack(pady=5)

frame = tk.LabelFrame(root, text="LabelFrame Container", padx=10, pady=10)
frame.pack(pady=10)
tk.Button(frame, text="Inside Frame 1").pack(side="left")
tk.Button(frame, text="Inside Frame 2").pack(side="left")

root.mainloop()
