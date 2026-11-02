import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, name TEXT, email TEXT, course TEXT)")
conn.commit()

root = Tk()
root.title("Student Details")

name = StringVar()
email = StringVar()
course = StringVar()
selected_id = StringVar()

Label(root, text="Name").grid(row=0, column=0)
Entry(root, textvariable=name).grid(row=0, column=1)
Label(root, text="Email").grid(row=1, column=0)
Entry(root, textvariable=email).grid(row=1, column=1)
Label(root, text="Course").grid(row=2, column=0)
Entry(root, textvariable=course).grid(row=2, column=1)

def clear_form():
    name.set("")
    email.set("")
    course.set("")
    selected_id.set("")

def show_all():
    listbox.delete(0, END)
    for row in cur.execute("SELECT * FROM student").fetchall():
        listbox.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def run(sql, values):
    cur.execute(sql, values)
    conn.commit()
    clear_form()
    show_all()

def add_record():
    run("INSERT INTO student(name, email, course) VALUES(?,?,?)",
        (name.get(), email.get(), course.get()))

def update_record():
    if not selected_id.get():
        messagebox.showwarning("Warning", "Select a record first")
    else:
        run("UPDATE student SET name=?, email=?, course=? WHERE id=?",
            (name.get(), email.get(), course.get(), selected_id.get()))

def delete_record():
    if not selected_id.get():
        messagebox.showwarning("Warning", "Select a record first")
    else:
        run("DELETE FROM student WHERE id=?", (selected_id.get(),))

def select_record(event):
    index = listbox.curselection()
    if index:
        parts = listbox.get(index[0]).split(" | ")
        selected_id.set(parts[0])
        name.set(parts[1])
        email.set(parts[2])
        course.set(parts[3])

Button(root, text="Add", command=add_record).grid(row=3, column=0)
Button(root, text="Update", command=update_record).grid(row=3, column=1)
Button(root, text="Delete", command=delete_record).grid(row=3, column=2)

listbox = Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=3)
listbox.bind("<<ListboxSelect>>", select_record)

show_all()
root.mainloop()
