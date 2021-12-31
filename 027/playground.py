from tkinter import *

def add(*args):
    total = 0
    for arg in args:
        try:
            total += arg
        except TypeError:
            pass
    return total

print(add(1, 2, 3, "a"))

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

button = Button(text="Click Me!", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()