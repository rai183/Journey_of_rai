import tkinter as tk
from tkinter import messagebox

def open_dashboard():
    # 1. Hide the main window
    root.withdraw()
    
    # 2. Create the second window (Toplevel)
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("300x200")
    
    tk.Label(dashboard, text="Welcome to the Second Window!", font=("Arial", 12)).pack(pady=20)
    
    # 3. Add a button to go back
    def go_back():
        dashboard.destroy() # Close the second window
        root.deiconify()    # Show the main window again
        
    tk.Button(dashboard, text="Logout / Go Back", command=go_back).pack()

# --- Main Window Setup ---
root = tk.Tk()
root.title("Main Login")
root.geometry("300x200")

tk.Label(root, text="Main Application Window", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Click below to proceed:").pack()

# This button triggers the switch
start_button = tk.Button(root, text="Enter Dashboard", command=open_dashboard, bg="blue", fg="white")
start_button.pack(pady=20)

root.mainloop()