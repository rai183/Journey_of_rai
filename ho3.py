import tkinter as tk

window = tk.Tk()
window.title("Rai's Profile")
window.geometry("600x600")
window.resizable(True, True)
window.configure(bg="#191970")

name_lbl = tk.Label(window, text="Name")
name_lbl.pack()

name_entry = tk.Entry(window)
name_entry.pack()


photo = tk.PhotoImage(file="cat.png")
img_label = tk.Label(window, image=photo)
img_label.pack(pady=10)

def show():
    name = name_entry.get()  
    if name:  
        new_window = tk.Toplevel(window)  
        new_window.title("Greeting Window")
        new_window.geometry("300x200")
        new_window.configure(bg="#191970")
        

        greeting_label = tk.Label(new_window, text=f"Hello, {name}!", font=("Arial", 16), bg="#191970", fg="white")
        greeting_label.pack(pady=20)
        
        img_label_new = tk.Label(new_window, image=photo)
        img_label_new.pack(pady=10)

button = tk.Button(window, text="Submit", command=show, fg="blue", state="normal", height=6, width=8, activebackground="blue")
button.pack()

window.mainloop()