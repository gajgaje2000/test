from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Registration Form")

name = StringVar()
email = StringVar()
password = StringVar()
country = StringVar()
language = StringVar(value="English")

Label(root, text="Name").grid(row=0, column=0)
Entry(root, textvariable=name).grid(row=0, column=1, columnspan=3)

Label(root, text="Email").grid(row=1, column=0)
Entry(root, textvariable=email).grid(row=1, column=1, columnspan=3)

Label(root, text="Password").grid(row=2, column=0)
Entry(root, textvariable=password, show="*").grid(row=2, column=1, columnspan=3)

Label(root, text="Country").grid(row=3, column=0)
ttk.Combobox(root, textvariable=country, values=["India", "USA", "UK"]).grid(row=3, column=1, columnspan=3)

Label(root, text="Language").grid(row=4, column=0)
Radiobutton(root, text="English", variable=language, value="English").grid(row=4, column=1)
Radiobutton(root, text="Hindi", variable=language, value="Hindi").grid(row=4, column=2)
Radiobutton(root, text="Gujarati", variable=language, value="Gujarati").grid(row=4, column=3)

def submit():
    if not name.get() or not email.get() or not password.get():
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo("Success", f"Registered: {name.get()}, {email.get()}, {country.get()}, {language.get()}")

Button(root, text="Register", command=submit).grid(row=5, column=1)

root.mainloop()
