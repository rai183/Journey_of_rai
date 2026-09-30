import tkinter as tk


def Gender_Color(choice):
    if choice ==1:
        window.config(bg="lightblue")
    elif choice ==2:
        window.config(bg="lightpink")
def After_Sumbit():
    First = str(First_Entry.get())
    Middle = str(Middle_Entry.get())
    Last = str(Last_Entry.get())

    Next_Window = tk.Toplevel()
    Next_Window.title("User Profile")
    Next_Window.configure(bg="lightgreen")
    Next_Window.resizable(False,False)
    Next_Window.geometry("300x480")

    gender = Choice.get()






window = tk.Tk()
window.title("Rai's Profile Builder")
window.geometry("600x250")
window.configure(bg="lightgreen")
window.resizable(False,False)

Window_Title = tk.Label(window, text = "Profile Builder", font = ("Arial", 10, "bold"))
Window_Title.pack()

#FRAME
Main_Frame = tk.Frame(window, width = 20, height=20)
Main_Frame.pack(pady = 5)

#ENTRY
First_Entry = tk.Entry(Main_Frame, width = 20).grid(row = 0, column = 0, pady = 5, padx = 20)
Middle_Entry = tk.Entry(Main_Frame, width = 20).grid(row = 0, column = 1, pady = 5, padx = 20)
Last_Entry = tk.Entry(Main_Frame, width = 20).grid(row = 0, column = 3, pady = 5, padx = 20)
Year_Entry = tk.Entry(Main_Frame, width = 20).grid(row = 3, column = 0, pady = 5, padx = 20)

#LABEL
First_label = tk.Label(Main_Frame, text = "First Name", font = ("Arial", 10)).grid(row = 1, column = 0, padx = 20)
Middle_label = tk.Label(Main_Frame, text = "Middle Name", font = ("Arial", 10)).grid(row = 1, column = 1, padx = 20)
Last_label = tk.Label(Main_Frame, text = "Last Name", font = ("Arial", 10)).grid(row = 1, column = 3, padx = 20)
Year_label = tk.Label(Main_Frame, text = "Birth Year", font = ("Arial", 10)).grid(row = 4, column = 0, padx = 20)
Gender_label = tk.Label(Main_Frame, text = "Gender", font = ("Arial", 10)).grid(row = 5, column = 0, padx = 20)
#BUTTON

tk.Button(Main_Frame, command=After_Sumbit)
tk.Button.pack(pady=5)
Choice=tk.IntVar()
Gender_Radio1=tk.Radiobutton(Main_Frame, text = "Female", font = ("Arial", 10),variable = Choice, command = lambda: Gender_Color(Choice.get()),value = 2)
Gender_Raidio2=tk.Radiobutton(Main_Frame, text = "Male", font = ("Arial", 10), variable = Choice, command=lambda: Gender_Color(Choice.get()),value = 1)
Gender_Radio1.grid(row=5,column=1,padx=20)
Gender_Raidio2.grid(row=5,column=2,padx=20)


window.mainloop()




















