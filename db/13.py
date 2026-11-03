from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient 

try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    client.admin.command("ping")
except Exception as e:
    print("MongoDB not connected:", e)
    raise SystemExit
col = client["bank"]["accounts"]

root = Tk()
root.title("Bank Account")

acc_no, name, balance, amount = StringVar(), StringVar(), StringVar(), StringVar()

for i, (text, var) in enumerate([("Account No", acc_no), ("Name", name),
                                 ("Balance", balance), ("Amount", amount)]):
    Label(root, text=text).grid(row=i, column=0)
    Entry(root, textvariable=var).grid(row=i, column=1, columnspan=2)

# 4. FUNCTIONS
def error(text):
    messagebox.showerror("Error", text)

def get_data():
    try:
        return {"acc_no": acc_no.get(), "name": name.get(), "balance": float(balance.get() or 0)}
    except ValueError:
        error("Balance must be a number")

def clear():
    for var in (acc_no, name, balance, amount):
        var.set("")

def show_all(): 
    listbox.delete(0, END)
    for d in col.find().sort("acc_no", 1):
        listbox.insert(END, d["acc_no"] + " | " + d["name"] + " | " + str(d["balance"]))

def create():
    data = get_data()
    if data is None:
        return
    if data["acc_no"] == "" or data["name"] == "":
        error("Enter account no and name")
    elif col.find_one({"acc_no": data["acc_no"]}):
        error("Account already exists")
    else:
        col.insert_one(data)
        clear()
        show_all()

def search():
    doc = col.find_one({"acc_no": acc_no.get()})
    if doc is None:
        error("Account not found")
    else:
        name.set(doc["name"])
        balance.set(doc["balance"])

def update(): 
    result = col.update_one({"acc_no": acc_no.get()}, {"$set": {"name": name.get()}})
    if result.matched_count == 0:
        error("Account not found")
    else:
        show_all()

def delete():
    result = col.delete_one({"acc_no": acc_no.get()})
    if result.deleted_count == 0:
        error("Account not found")
    else:
        clear()
        show_all()

def transaction(sign):
    doc = col.find_one({"acc_no": acc_no.get()})
    try:
        amt = float(amount.get())
    except ValueError:
        amt = 0
    if doc is None:
        error("Account not found")
    elif amt <= 0:
        error("Enter an amount greater than 0")
    elif doc["balance"] + sign * amt < 0:
        error("Insufficient balance")
    else:
        col.update_one({"acc_no": acc_no.get()}, {"$inc": {"balance": sign * amt}})
        search()
        show_all()

def select(event):
    index = listbox.curselection()
    if index:
        acc_no.set(listbox.get(index[0]).split(" | ")[0])
        search()

buttons = [("Create", create), ("Search", search), ("Update", update),
           ("Deposit", lambda: transaction(1)), ("Withdraw", lambda: transaction(-1)),
           ("Delete", delete), ("Display", show_all), ("Clear", clear), ("Exit", root.destroy)]
for i, (text, command) in enumerate(buttons):
    Button(root, text=text, width=10, command=command).grid(row=4 + i // 3, column=i % 3)

listbox = Listbox(root, width=45)
listbox.grid(row=7, column=0, columnspan=3)
listbox.bind("<<ListboxSelect>>", select)

show_all()
root.mainloop()
