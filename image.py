import tkinter as tk

window=tk.Tk()
window.title("Image Testing")
window.geometry("500x500")
window.resizable(True, False)
window.configure(bg="white")

photo = tk.PhotoImage(file= "cat.png")
img_label = tk.Label(window, image=photo) 
img_label.pack(pady=10)
small_photo = photo.subsample(2,2)
img_label = tk.Label(window, image=small_photo)
window.mainloop()