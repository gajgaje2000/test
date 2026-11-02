from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("More Tkinter Widgets")
root.geometry("400x520")

def say_hello():
    messagebox.showinfo("Menu", "Hello from the menu")

menubar = Menu(root)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Say hello", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Widget demo"))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

Message(root, text="Message widget wraps long text automatically.", width=300, bg="lightyellow").pack(pady=5)

course = StringVar(value="None")
mb = Menubutton(root, text="Choose Course", relief=RAISED)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_radiobutton(label="MCA", variable=course, value="MCA")
mb.menu.add_radiobutton(label="BCA", variable=course, value="BCA")
mb.pack(pady=3)
Label(root, textvariable=course).pack()

lf = LabelFrame(root, text="Spinbox: semester", padx=10, pady=5)
lf.pack(fill=X, padx=10, pady=5)
spin = Spinbox(lf, from_=1, to=6, width=5)
spin.pack(side=LEFT)

def show_spin():
    messagebox.showinfo("Spinbox", "Semester: " + spin.get())

Button(lf, text="Show value", command=show_spin).pack(side=LEFT, padx=10)

frame = Frame(root)
frame.pack(pady=5)
scroll = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, height=4, yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
for i in range(1, 21):
    listbox.insert(END, "Item " + str(i))
listbox.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

pw = PanedWindow(root, orient=HORIZONTAL, sashrelief=RAISED, height=80)
pw.pack(fill=BOTH, expand=True, padx=10, pady=5)
pw.add(Label(pw, text="Left pane", bg="lightblue"))
pw.add(Label(pw, text="Right pane", bg="lightgreen"))

Button(root, text="Exit", command=root.destroy).pack(pady=5)

root.mainloop()
