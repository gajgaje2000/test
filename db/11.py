from tkinter import *

root = Tk()
root.title("Widget Attributes")

label = Label(root, text="Styled Label", bg="navy", fg="white", font=("Arial", 16, "bold"),
              width=20, height=2, relief=RAISED, bd=4, padx=10, pady=5)
label.pack(pady=5)

for style in [FLAT, RAISED, SUNKEN, GROOVE, RIDGE]:
    Label(root, text=style, relief=style, bd=3, width=12).pack(pady=1)

entry = Entry(root, width=25, bd=3, justify=CENTER, bg="lightyellow", fg="black", font=("Courier", 12))
entry.insert(0, "Entry")
entry.pack(pady=5)

button = Button(root, text="Click Me", bg="green", fg="white", activebackground="darkgreen",
                cursor="hand2", width=15, bd=5)
button.pack(pady=5)

text_box = Text(root, width=30, height=3, bg="lightgrey", fg="blue", wrap=WORD)
text_box.insert(END, "Text widget with wrap, width and height.")
text_box.pack(pady=5)

def change():
    label.config(bg="red", text="Changed!")
    print("bg is now:", label.cget("bg"))

def toggle():
    if button["state"] == NORMAL:
        button.config(state=DISABLED)
    else:
        button.config(state=NORMAL)

Button(root, text="Change label", command=change).pack(pady=3)
Button(root, text="Enable / Disable", command=toggle).pack(pady=3)

root.mainloop()
