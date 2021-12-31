from json.decoder import JSONDecodeError
import os
from tkinter import *
from tkinter import messagebox
import string
import random
import json
import shutil

LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation


def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo("Invalid form entry", "Form values must not be empty.")
    else:
        try:
            with open("./passwords.json", "r") as f:
                password_data = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo("Info", "No password data saved.")
        except JSONDecodeError:
            messagebox.showerror("Critical Error", "passwords.json is corrupt, please investigate or remove file")
            shutil.copy("./passwords.json", ".passwords.backup.json")
        else:
            if website in password_data:
                details = password_data[website]
                user = details.get("user")
                password = details.get("password")
                messagebox.showinfo("Info", f"E-mail/User: {user}\nPassword: {password}\n Password saved to clipboard.")
                window.clipboard_clear()
                window.clipboard_append(password)
            else:
                messagebox.showinfo("Info", f"No password saved for {website}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator(length: int=32) -> str:
    '''
    Generates a random password having the specified length
    :length -> length of password to be generated. Defaults to 16
        if nothing is specified.
    :returns string <class 'str'>
    '''

    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    printable = list(printable)
    random_password = ""

    random_password = "".join([random.choice(printable) for _ in range(length)])

    return random_password


def generate_password():
    password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    window.clipboard_clear()
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    password_object = {website: {"user": user, "password": password}}
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo("Invalid form entry", "Form values must not be empty.")
    else:
        if messagebox.askokcancel(title=website, message=f"These are the details entered: \nE-mail/user: {user}\nPassword: {password}\nIs it ok to save?"):
            try:
                with open("./passwords.json", "r") as f:
                    password_data = json.load(f)
            except FileNotFoundError:
                password_data = {}
            except JSONDecodeError:
                messagebox.showerror("Critical Error", "passwords.json is corrupt, please investigate or remove file")
                shutil.copy("./passwords.json", ".passwords.backup.json")
                password_data = {}
            finally:
                with open("./passwords.json", "w") as f:
                    password_data.update(password_object)
                    json.dump(password_data, f, indent=4)
                window.clipboard_clear()
                window.clipboard_append(password)
                website_entry.delete(0, END)
                user_entry.delete(0, END)
                password_entry.delete(0, END)
                user_entry.insert(0, string="josh@example.com")
                messagebox.showinfo("Password successfully saved", "Password successfully saved.\nPassword has been copied to your clipboard.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

directory = os.path.realpath(__file__ + f"/{os.pardir}")
logo = PhotoImage(file=f"{directory}/logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

WEBSITE_ROW = 1
USER_ROW = 2
PASSWORD_ROW = 3
LABEL_COLUMN = 0
ENTRY_COLUMN = 1

website_label = Label(text="Website:")
website_label.grid(column=LABEL_COLUMN, row=WEBSITE_ROW)

user_label = Label(text="E-mail/Username:")
user_label.grid(column=LABEL_COLUMN, row=USER_ROW)

password_label = Label(text="Password:")
password_label.grid(column=LABEL_COLUMN, row=PASSWORD_ROW)

add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(column=ENTRY_COLUMN, row=4, columnspan=2)

generate_password_button = Button(text="Generate Password", width=13, command=generate_password)
generate_password_button.grid(column=2, row=PASSWORD_ROW)

search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=WEBSITE_ROW)

website_entry = Entry(width=18)
website_entry.grid(column=ENTRY_COLUMN, row=WEBSITE_ROW)
website_entry.focus()

user_entry = Entry(width=35)
user_entry.insert(END, string="josh@example.com")
user_entry.grid(column=ENTRY_COLUMN, row=USER_ROW, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(column=ENTRY_COLUMN, row=PASSWORD_ROW)

window.mainloop()