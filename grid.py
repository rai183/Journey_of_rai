import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.configure(bg = "grey")

user_label = tk.Label(window, text = "User From")
user_label.grid(column = 0, row = 0, columnspan = 3)

u_label = tk.Label(window, text = "User:")
u_label.grid(column = 0, row = 1)

u_entry = tk.Entry(window)
u_entry.grid(column = 1, row = 1, columnspan = 2)


window.mainloop()
