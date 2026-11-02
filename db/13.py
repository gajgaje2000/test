from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    client.admin.command("ping")
except Exception as e:
    print("MongoDB connection failed:", e)
    raise SystemExit
col = client["bank"]["accounts"]

root = Tk()
root.title("Bank Account Management")

acc_no = StringVar()
name = StringVar()
balance = StringVar()
amount = StringVar()

for i, (text, var) in enumerate([("Account No", acc_no), ("Holder Name", name),
                                 ("Balance", balance), ("Amount", amount)]):
    Label(root, text=text).grid(row=i, column=0, sticky="w", padx=5)
    Entry(root, textvariable=var).grid(row=i, column=1, columnspan=2, sticky="ew", padx=5, pady=2)

def to_number(text):
    try:
        value = float(text)
    except ValueError:
        return None
    return value if value >= 0 else None

def find():
    doc = col.find_one({"acc_no": acc_no.get()})
    if doc is None:
        messagebox.showerror("Error", "Account not found")
    return doc

def show_all():
    listbox.delete(0, END)
    for d in col.find().sort("acc_no", 1):
        listbox.insert(END, d["acc_no"] + " | " + d["name"] + " | " + str(d["balance"]))

def clear():
    for var in (acc_no, name, balance, amount):
        var.set("")

def create():
    opening = to_number(balance.get() or "0")
    if acc_no.get() == "" or name.get() == "" or opening is None:
        messagebox.showerror("Error", "Enter account no, name and a valid balance")
    elif col.find_one({"acc_no": acc_no.get()}):
        messagebox.showerror("Error", "Account already exists")
    else:
        col.insert_one({"acc_no": acc_no.get(), "name": name.get(), "balance": opening})
        clear()
        show_all()

def search():
    doc = find()
    if doc:
        name.set(doc["name"])
        balance.set(doc["balance"])

def update():
    if find():
        col.update_one({"acc_no": acc_no.get()}, {"$set": {"name": name.get()}})
        show_all()

def delete():
    result = col.delete_one({"acc_no": acc_no.get()})
    if result.deleted_count == 0:
        messagebox.showerror("Error", "Account not found")
    else:
        clear()
        show_all()

def deposit():
    amt = to_number(amount.get())
    if not amt:
        messagebox.showerror("Error", "Enter an amount greater than 0")
    elif find():
        col.update_one({"acc_no": acc_no.get()}, {"$inc": {"balance": amt}})
        search()
        show_all()

def withdraw():
    amt = to_number(amount.get())
    if not amt:
        messagebox.showerror("Error", "Enter an amount greater than 0")
        return
    doc = find()
    if doc:
        if amt > doc["balance"]:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            col.update_one({"acc_no": acc_no.get()}, {"$inc": {"balance": -amt}})
            search()
            show_all()

def select(event):
    index = listbox.curselection()
    if index:
        acc_no.set(listbox.get(index[0]).split(" | ")[0])
        search()

buttons = [("Create", create), ("Search", search), ("Update", update),
           ("Deposit", deposit), ("Withdraw", withdraw), ("Delete", delete),
           ("Display", show_all), ("Clear", clear), ("Exit", root.destroy)]
for i, (text, command) in enumerate(buttons):
    Button(root, text=text, width=10, command=command).grid(row=4 + i // 3, column=i % 3, padx=3, pady=3)

listbox = Listbox(root, width=45)
listbox.grid(row=7, column=0, columnspan=3, padx=5, pady=5)
listbox.bind("<<ListboxSelect>>", select)

show_all()
root.mainloop()
