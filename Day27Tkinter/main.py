from tkinter import *


def calculate():
    miles = entry.get()
    km = float(miles)*1.6
    km_label.config(text=str(km))


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)

# Label
my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

# Entry box
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

second_label = Label(text="is equal to")
second_label.grid(column=0, row=1)

km_label = Label(text=f"{0}")
km_label.grid(column=1, row=1)

km_unit_label = Label(text="Km")
km_unit_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
