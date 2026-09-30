import tkinter as tk

#Initializing the main window
window = tk.Tk()
window.title("Profile Builder")
window.configure(bg="lightgreen")

#function for computing age in the main window
def compute_age(event):
    year=int(birth_entry.get())
    age= 2026-year
    age_label['text']= f"You are {age} years old."
#Function for Gender-based color
def change_color():
    gender=int(gender_var.get())
    if gender == 1:
        window ['bg'] = "lightblue"
        title ['bg'] = "lightblue"
    else:
        window ['bg'] = "lightpink"
        title ['bg'] = "lightpink"
#Function for button hover
def on_enter(event):
    button['bg'] = "lightblue"
#Function for reverting color when mouse leaves
def on_leave(event):
    button['bg'] = "lightgreen"
#Function for Opening the Profile window
def open_profile_card():
    profile_card = tk.Toplevel(window)
    profile_card.title("Student ID")
    #contents of the profile card
    fname=fname_entry.get()
    mname=mname_entry.get()
    lname=lname_entry.get()
    name = fname[0].upper()+fname[1:] + " " + mname[0].upper() + ". " + lname[0].upper()+lname[1:]
    year=int(birth_entry.get())
    age= 2026-year
    gender_value = gender_var.get()
    #Defining bg of Toplevel based on the gender
    if gender_value == 1:
        gender = "Male"
        profile_card ['bg'] = "lightblue"
    else:
        gender ="Female"
        profile_card ['bg'] = "lightpink"
        
    prof_title = tk.Label(profile_card, text="Student ID", font=("Times New Roman",16,"bold"),bg=profile_card['bg'])
    prof_title.grid(row=0,column=0,columnspan=3,pady=(20,0),sticky="nsew")

    profile_frame = tk.Frame(profile_card, bg="#E6E6FA", bd=2, relief="groove")
    profile_frame.grid(row=1,column=0,padx=10,pady=10)

    picture=tk.PhotoImage(file="trials/userlogo.png")
    picture = picture.subsample(10,10)

    pic_label = tk.Label(profile_frame, image=picture)
    pic_label.image = picture
    pic_label.grid(row=2,column=0,columnspan=2,pady=10)

    name_label = tk.Label(profile_frame, text="Name: ", font=("Questrial",14),bg="#E6E6FA")
    name_label.grid(row=3,column=0,pady=(10,0),sticky="w")

    name_value = tk.Label(profile_frame, text=name, font=("Questrial",14),bg="#E6E6FA")
    name_value.grid(row=3,column=1,columnspan=2,pady=(10,0))

    age_label = tk.Label(profile_frame, text="Age: ", font=("Questrial",14),bg="#E6E6FA")
    age_label.grid(row=4,column=0,pady=(10,0),sticky="w")

    age_value = tk.Label(profile_frame, text=f"{age} years old", font=("Questrial",14),bg="#E6E6FA")
    age_value.grid(row=4,column=1,pady=(10,0))

    gender_label = tk.Label(profile_frame, text="Gender: ", font=("Questrial",14),bg="#E6E6FA") 
    gender_label.grid(row=5,column=0,columnspan=2,pady=(10,0),sticky="w")
   
    gender_value = tk.Label(profile_frame, text=gender, font=("Questrial",14),bg="#E6E6FA") 
    gender_value.grid(row=5,column=1,columnspan=2,pady=(10,0))

#Contents for the main window
title = tk.Label ( window, text="Profile Builder", font=("Times New Roman",14,"bold"),bg="lightgreen")
title.grid(row=0, column=0, columnspan=6)

genframe = tk.Frame(window,bg="lightgreen",bd=2, relief="groove")
genframe.grid(row=1,column=0, columnspan=6,padx=10,pady=10)

fname_entry = tk.Entry(genframe, font=("Poppins",12))
fname_entry.grid(row=2, column=1,columnspan=2,padx=(10,0),pady=(10,0))

fname_label = tk.Label(genframe, text="First Name", font=("Poppins",10,"italic"),bg="lightgreen")
fname_label.grid(row=3, column=1,columnspan=2)

mname_entry = tk.Entry(genframe, font=("Poppins",12))
mname_entry.grid(row=2, column=3,columnspan=2,padx=(10,0),pady=(10,0))

mname_label = tk.Label(genframe, text="Middle Name", font=("Poppins",10,"italic"),bg="lightgreen")
mname_label.grid(row=3, column=3,columnspan=2)

lname_entry = tk.Entry(genframe, font=("Poppins",12))
lname_entry.grid(row=2, column=5,columnspan=2,padx=(10,10),pady=(10,0))

lname_label = tk.Label(genframe, text="Last Name", font=("Poppins",10,"italic"),bg="lightgreen")
lname_label.grid(row=3, column=5,columnspan=2)

birth_entry = tk.Entry(genframe, font=("Poppins",12))
birth_entry.grid(row=4, column=1,columnspan=2,padx=(10,0))

birthyear_label = tk.Label(genframe, text="Birth Year", font=("Poppins",10,"italic"),bg="lightgreen")
birthyear_label.grid(row=5, column=2,columnspan=2)

age_label = tk.Label(genframe, text="Computing Age...", font=("Poppins",16,"italic"),bg="lightgreen",bd=2,relief="raised")
age_label.grid(row=4, column=4,columnspan=4,rowspan=2)


gender_label = tk.Label(genframe, text="Gender", font=("Poppins",10,"italic"),bg="lightgreen")
gender_label.grid(row=6, column=0,columnspan=2)

gender_var = tk.IntVar()
male= tk.Radiobutton(genframe,text="Male", variable=gender_var, value = 1, font=("Poppins",10),bg="lightgreen",command=change_color)
male.grid(row=6, column=2)

female= tk.Radiobutton(genframe,text="Female", variable=gender_var, value = 0, font=("Poppins",10),bg="lightgreen",command=change_color)
female.grid(row=6, column=4)

button= tk.Button(window,text="Submit",font=("Poppins",12,"bold"),bg="lightpink",command=open_profile_card)
button.grid(row=7, column=0, columnspan=6,pady=(10,20))

#binding events
birth_entry.bind("<Return>",compute_age) #automatically calculates age when Enter is pressed
button.bind("<Enter>", on_enter) # changes button color when mouse hovers on button
button.bind("<Leave>", on_leave) # reverts original button color

#enter the mainloop
window.mainloop()