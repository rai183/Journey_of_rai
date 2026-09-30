import tkinter as tk

window = tk.Tk()
window.title("Rai's Calculator")
window.resizable(False, False)
window.configure(bg ="gray")


#LABEL
result_label = tk.Label(window, text = "Results Appear Here", bg = "white", font = ("Arial", 8), width = 20)
result_label.grid(row=0, column = 0, columnspan = 2, pady = 5, sticky = "ew")

tk.Label(window, text = "Enter 1st Number: ", bg = "white", fg = "black", font = ("Arial", 8), width = 10).grid(row = 1, column = 0, padx = 5, pady = 5)
tk.Label(window, text = "Enter 2nd Number: ", bg = "white", fg = "black", font = ("Arial", 8), width = 10).grid(row = 2, column = 0, padx = 5, pady = 5)

#ENTRY
entry1 = tk.Entry(window, width = 10)
entry1.grid(row = 1, column = 1)
entry2 = tk.Entry(window, width = 10)
entry2.grid(row = 2, column = 1)

#DEF
def add():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text = f"the Sum of {a} + {b} is {a+b}")
def subract(): 
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text = f"The Difference of {a} - {b} is {a-b}")
def multiply():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text =f"The Product of {a} * {b} is {a*b}")
def divide():
    a = float(entry1.get())
    b = float(entry2.get())
    result_label.config(text = f"the Quotient of {a} / {b} is {a/b}")

#BUTTON
tk.Button(window, text = "ADD", width = 12, command = add).grid(row = 3, column = 0, pady = 10)
tk.Button(window, text = "SUBTRACTION", width = 12, command = add).grid(row = 3, column = 1, pady = 10)
tk.Button(window, text = "MULTIPLY", width = 12, command = add).grid(row = 4, column = 0, pady = 10)
tk.Button(window, text = "DIVIDE", width = 12, command = add).grid(row = 4, column = 1, pady = 10)

window.mainloop()