import tkinter as tk

window = tk.Tk()

window.title("Miss u kyedae and tenz balik na kayo pls")
window.geometry("1500x1000")
window.resizable(False, False)
window.configure(bg = "navyblue")


label = tk.Label(window, text="mi casa is su casa tkinter", font = ("Times New Roman", "10", "bold"), fg = "blue", width = 50, height = 3, anchor = "center")
label.pack()

window.mainloop()

