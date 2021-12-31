from tkinter import *

#Creating a new window and configurations
window = Tk()
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

answer_label = Label(text="0")
answer_label.grid(column=0, row=2)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)

def convert():
    miles = 0.0
    try:
        miles = float(entry.get())
    except ValueError:
        miles = 0.0
    kilometers = miles * 1.609344
    answer_label.config(text=kilometers)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

window.mainloop()
