from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Information")

name = StringVar()
email = StringVar()
phone = StringVar()
classname = StringVar(value="FY")
reading = IntVar()
music = IntVar()
sports = IntVar()

Label(root, text="Name").grid(row=0, column=0)
Entry(root, textvariable=name).grid(row=0, column=1, columnspan=3)

Label(root, text="Email").grid(row=1, column=0)
Entry(root, textvariable=email).grid(row=1, column=1, columnspan=3)

Label(root, text="Phone").grid(row=2, column=0)
Entry(root, textvariable=phone).grid(row=2, column=1, columnspan=3)

Label(root, text="Address").grid(row=3, column=0)
address = Text(root, width=20, height=3)
address.grid(row=3, column=1, columnspan=3)

Label(root, text="Class").grid(row=4, column=0)
Radiobutton(root, text="FY", variable=classname, value="FY").grid(row=4, column=1)
Radiobutton(root, text="SY", variable=classname, value="SY").grid(row=4, column=2)
Radiobutton(root, text="TY", variable=classname, value="TY").grid(row=4, column=3)

Label(root, text="Semester").grid(row=5, column=0)
semester = Listbox(root, height=3, exportselection=False)
semester.insert(END, "Sem 1", "Sem 2", "Sem 3", "Sem 4")
semester.grid(row=5, column=1, columnspan=3)

Label(root, text="Hobbies").grid(row=6, column=0)
Checkbutton(root, text="Reading", variable=reading).grid(row=6, column=1)
Checkbutton(root, text="Music", variable=music).grid(row=6, column=2)
Checkbutton(root, text="Sports", variable=sports).grid(row=6, column=3)

Label(root, text="Image").grid(row=7, column=0)
canvas = Canvas(root, width=100, height=70, bg="white")
canvas.create_oval(20, 10, 80, 60, fill="skyblue")
canvas.grid(row=7, column=1, columnspan=3)

def submit():
    hobbies = []
    if reading.get():
        hobbies.append("Reading")
    if music.get():
        hobbies.append("Music")
    if sports.get():
        hobbies.append("Sports")

    sem = ""
    index = semester.curselection()
    if index:
        sem = semester.get(index[0])

    messagebox.showinfo("Submitted",
                        f"Name: {name.get()}\n"
                        f"Email: {email.get()}\n"
                        f"Phone: {phone.get()}\n"
                        f"Address: {address.get('1.0', END).strip()}\n"
                        f"Class: {classname.get()}\n"
                        f"Semester: {sem}\n"
                        f"Hobbies: {', '.join(hobbies)}")

Button(root, text="Submit", command=submit).grid(row=8, column=1)

root.mainloop()
