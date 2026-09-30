import tkinter as tk

def Gender_Color(Choice):
    if Choice == 1:
        window.configure(bg="lightblue")
    elif Choice == 2:
        window.configure(bg="lightpink")

def Age_Calculator(*args):
    Age = 2026 - int(Year_Entry_Var.get())
    if int:
        Age_Label.configure(text=str(f"You are {Age} years old!"))
    else:
        Age_Label.configure(text="Your age is...")

def After_Submit():
    First = str(First_Entry.get())
    Last = str(Last_Entry.get())
    Initial = str(Initial_Entry.get())

    Another_Window = tk.Toplevel()
    Another_Window.title("Profile")
    Another_Window.resizable(False,False)
    Another_Window.geometry("300x480")
    Another_Window.configure(bg="lightgreen")

    #img = tk.PhotoImage(file="logo2.png")
    #img = img.subsample(3,3) 

    #image_label = tk.Label(Another_Window, image = img)

    gender = Choice.get()
    if gender == 1:
        Another_Window.configure(bg="lightblue")
    elif gender == 2:
        Another_Window.configure(bg="lightpink")

    try:
        Age = 2026 - int(Year_Entry_Var.get())
    except ValueError:
        Age = "N/A"

    Another_Window_Title = tk.Label(Another_Window,
                                    text="Profile",
                                    font=("Arial",15,"bold"),
                                    bg=(Another_Window["bg"]),     
                                    )
    Name = tk.Label(Another_Window,
                                    text=(f"Name: {First} {Initial} {Last}"),
                                    font=("Arial",15),
                                    bg=(Another_Window["bg"]),                                
                                    )

    Age2 = tk.Label(Another_Window,
                                    text=(f"Age: {Age} Years old"),
                                    font=("Arial",15),
                                    bg=(Another_Window["bg"]),                               
                                    )
    gender2 = tk.Label(Another_Window,
                                    text=("Gender: N/A"),
                                    font=("Arial",15),
                                    bg=(Another_Window["bg"]),                               
                                    )          
    
    if gender == 1:
        gender2.configure(text="Gender: Male")
    elif gender == 2:
        gender2.configure(text="Gender: Female")

    Another_Window_Title.pack(pady=5)
    #image_label.pack(pady=5)
    Name.pack(pady=5,padx=10,anchor="w")
    Age2.pack(pady=5,padx=10,anchor="w")
    gender2.pack(pady=5,padx=10,anchor="w")
    
    
    Another_Window.mainloop()

window = tk.Tk()
window.title("Profile Builder")
window.geometry("600x250")
window.resizable(False,False)
window.configure(bg="lightgreen")

Year_Entry_Var = tk.StringVar()
Year_Entry_Var.trace('w', Age_Calculator)

Window_Title = tk.Label(window,
text="Profile Builder",
font=("Arial",10,"bold"),
)

Main_Frame = tk.Frame(window)

First_Entry = tk.Entry(Main_Frame,
width=20
)
Last_Entry = tk.Entry(Main_Frame,
width=20
)
Initial_Entry = tk.Entry(Main_Frame,
width=20
)
Year_Entry = tk.Entry(Main_Frame,
width=20,
textvariable=Year_Entry_Var
)

First_Label = tk.Label(Main_Frame,
text="First Name",
font=("Arial",10)
)
Last_Label = tk.Label(Main_Frame,
text="Last Name",
font=("Arial",10)
)
Initial_Label = tk.Label(Main_Frame,
text="Middle Name",
font=("Arial",10)
)
Year_Label = tk.Label(Main_Frame,
text="Birth Year",
font=("Arial",10)
)
Age_Label = tk.Label(Main_Frame,
text="Your Age is...",
font=("Arial",14,"bold")
)
Gender_Label = tk.Label(Main_Frame,
text="Gender",
font=("Arial",10)
)

Choice = tk.IntVar()
Gender_Radio1 = tk.Radiobutton(Main_Frame,
text="Male",
font=("Arial",10),
variable=Choice,
command=lambda: Gender_Color(Choice.get()),
value=1
)

Gender_Radio1.deselect()
Gender_Radio2 = tk.Radiobutton(Main_Frame,
text="Female",
font=("Arial",10),
variable=Choice,
command=lambda: Gender_Color(Choice.get()),
value=2
)
Gender_Radio2.deselect()

Submit_Button = tk.Button(window,
                          text="Submit",
                          font=("Arial",12,"bold"),
                          width=10,
                          height=2,
                          fg="white",
                          bg="Gray",
                          activeforeground="black",
                          activebackground="orange",
                          command=After_Submit
                          )

Window_Title.pack(pady=5)
Main_Frame.pack(pady=5)

First_Entry.grid(column=0,row=0,pady=5,padx=20)
Last_Entry.grid(column=1,row=0,pady=5,padx=20)
Initial_Entry.grid(column=2,row=0,pady=5,padx=20)
Year_Entry.grid(column=0,row=3,pady=5,padx=20)

First_Label.grid(column=0,row=1,padx=20)
Last_Label.grid(column=1,row=1,padx=20)
Initial_Label.grid(column=2,row=1,padx=20)
Year_Label.grid(column=0,row=4,padx=20)
Age_Label.grid(column=1,columnspan=2,row=3,rowspan=2,padx=20)
Gender_Label.grid(column=0,row=5,padx=20,pady=5)

Gender_Radio1.grid(column=1,row=5,padx=20)
Gender_Radio2.grid(column=2,row=5,padx=20)

Submit_Button.pack(pady=5)

window.mainloop()