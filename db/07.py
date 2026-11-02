from tkinter import *

root = Tk()
root.title("Tkinter Practice")

def blank_window():
    w = Toplevel(root)
    w.geometry("300x200")

def pack_window():
    w = Toplevel(root)
    Button(w, text="Top").pack()
    Button(w, text="Left").pack(side=LEFT)
    Button(w, text="Right").pack(side=RIGHT)

def grid_login():
    w = Toplevel(root)
    Label(w, text="Username").grid(row=0, column=0)
    Entry(w).grid(row=0, column=1)
    Label(w, text="Password").grid(row=1, column=0)
    Entry(w, show="*").grid(row=1, column=1)
    Button(w, text="Login").grid(row=2, column=1)

def place_window():
    w = Toplevel(root)
    w.geometry("300x150")
    Label(w, text="Name").place(x=20, y=20)
    Entry(w).place(x=80, y=20)
    Button(w, text="Submit").place(x=80, y=60)

def frame_window():
    w = Toplevel(root)
    w.geometry("300x100")
    left = Frame(w, bg="lightblue")
    right = Frame(w, bg="lightgreen")
    left.pack(side=LEFT, fill=BOTH, expand=True)
    right.pack(side=RIGHT, fill=BOTH, expand=True)
    Label(left, text="Left part").pack()
    Label(right, text="Right part").pack()

def widgets_window():
    w = Toplevel(root)
    Label(w, text="Label").pack()

    entry = Entry(w)
    entry.pack()
    Button(w, text="Print entry", command=lambda: print(entry.get())).pack()

    Checkbutton(w, text="Python").pack()

    choice = StringVar(value="MCA")
    Radiobutton(w, text="MCA", variable=choice, value="MCA").pack()
    Radiobutton(w, text="BCA", variable=choice, value="BCA").pack()

    listbox = Listbox(w, height=3)
    listbox.insert(END, "Sem 1", "Sem 2", "Sem 3")
    listbox.pack()

    Text(w, height=3, width=25).pack()
    Scale(w, from_=0, to=100, orient=HORIZONTAL).pack()
    Button(w, text="Open Toplevel", command=lambda: Toplevel(w)).pack()

def calculator_window():
    w = Toplevel(root)
    a = Entry(w)
    b = Entry(w)
    result = Label(w, text="Result")
    a.pack()
    b.pack()
    result.pack()

    def add_numbers():
        result.config(text=float(a.get()) + float(b.get()))

    Button(w, text="Add", command=add_numbers).pack()

for text, func in [("Blank window", blank_window), ("pack()", pack_window),
                   ("grid() login", grid_login), ("place()", place_window),
                   ("Frames", frame_window), ("Widgets", widgets_window),
                   ("Calculator", calculator_window)]:
    Button(root, text=text, command=func).pack()

root.mainloop()
