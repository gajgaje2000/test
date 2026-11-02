from tkinter import *

root = Tk()
root.title("Resize Handling")
root.geometry("400x300")
root.minsize(250, 200)
root.maxsize(700, 500)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

size_label = Label(root, bg="yellow")
size_label.grid(row=0, column=0, columnspan=2, sticky="ew")
Text(root, bg="lightblue").grid(row=1, column=0, sticky="nsew")
Listbox(root, bg="lightgreen").grid(row=1, column=1, sticky="nsew")
Label(root, text="place: stays centered", bg="orange").place(relx=0.5, rely=0.5, anchor=CENTER)

def on_resize(event):
    if event.widget == root:
        size_label.config(text=f"Size: {event.width} x {event.height}")

root.bind("<Configure>", on_resize)
root.mainloop()
