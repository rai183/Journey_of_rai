import tkinter as tk



window = tk.Tk()
window.title("Rai's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg = "#191970")

name_lbl=tk.Label(window, text="Name")
name_lbl.pack()

name_entry=tk.Entry(window)
name_entry.pack()

name_entry=tk.Entry(window,show="*",state="disabled")
name_entry.pack()

name=name_entry.get()

photo = tk.PhotoImage(file= "cat.png")
img_label = tk.Label(window, image=photo) 
img_label.pack(pady=10)


def show():
    img_label['text'] = (f"Hello,{name}")

button = tk.Button (window,text="Submit",command=show,fg="blue",state="normal",height=6,width=8,activebackground="blue")
button.pack()

window.mainloop()