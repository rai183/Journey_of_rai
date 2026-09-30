import tkinter as tk
from tkinter import ttk  
import threading
import time

def simulate_loading(progress_bar, root):

    total_steps = 100
    for i in range(total_steps + 1):
        progress_bar['value'] = i

        root.update_idletasks()

        time.sleep(0.05)

    root.destroy()

def create_loading_screen():

    loading_root = tk.Tk()
    loading_root.title("Loading...")

    window_width = 400
    window_height = 100

    screen_width = loading_root.winfo_screenwidth()
    screen_height = loading_root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    loading_root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    loading_root.overrideredirect(True)
    loading_label = tk.Label(
        loading_root,
        text="PROCESSING...",
        font=("Arial", 20)
    )
    loading_label.pack(pady=5)

    progress = ttk.Progressbar(
        loading_root,
        orient='horizontal',
        length=300,
        mode='determinate' 
    )
    progress.pack(pady=5)

    loading_thread = threading.Thread(
        target=simulate_loading,
        args=(progress, loading_root)
    )
    loading_thread.start()

    loading_root.mainloop()

if __name__ == "__main__":
    create_loading_screen()