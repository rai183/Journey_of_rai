
import tkinter as tk



window = tk.Tk()
window.title("Rai's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg = "#191970")

Title = tk.Label(text = "Student Profile", font = ("Times New Roman", 20), bg="#191970", fg = "#F9F9FC")
Name = tk.Label(text = "Raizere Angelo Monton Gañac", font = ("Times New Roman", 20), bg="#191970", fg = "#F9F9FC")
Age = tk.Label(text ="Age: 18", font = ("Times New Roman", 20), bg="#191970", fg = "#F9F9FC")
Address = tk.Label(text = "Barangay Kanlurang Mayao, Lucena City", font = ("Times New Roman", 20), bg="#191970", fg = "#F9F9FC")
Course = tk.Label(text = "Bachelor of Science in Information Technology", font = ("Times New Roman",20), bg="#191970", fg = "#F9F9FC")
Birthday = tk.Label(text = "April 10, 2007", font = ("Times New Roman", 20), bg="#191970", fg = "#F9F9FC")
Quote = tk.Label(text = "If it's meant to be, it will be", font = ("Times New Roman", 20), bg = "#191970", fg = "#F9F9FC")


Title.pack(pady=10)
Name.pack(pady=5, anchor='nw')
Age.pack(pady=5,anchor='nw')
Address.pack(pady=5,anchor='nw')
Course.pack(pady=5, anchor='nw')
Birthday.pack(pady=5, anchor='nw')
Quote.pack(pady=5, anchor='nw')

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple" ] 
color_index = 0
fonts = [
    ("Times New Roman", 20),
    ("Arial", 20, "bold"),
    ("Courier New", 20, "italic"),
    ("Verdana", 20, "bold"),
    ("Impact", "bold", 20)
]
color_index = 0
font_index = 0

def animate_quote():
    global color_index, font_index

    Quote.config(
    fg=colors[color_index], 
    font=fonts[font_index]) 
    color_index = (color_index + 1) % len(colors)
    font_index = (font_index + 1) % len(fonts)
    
    window.after(700, animate_quote)

animate_quote()
def animate_text():
    global color_index
    Quote.config(fg=colors[color_index])
    color_index = (color_index + 1) % len(colors)
    window.after(500, animate_text)

animate_text()

photo = tk.PhotoImage(file= "cat.png")
img_label = tk.Label(window, image=photo) 
img_label.pack(pady=10)

window.mainloop()


