from tkinter import *
from tkinter import messagebox
import random
import json


#  FIND PASSWORD

def find_password():
    try:
        file = open("data.json", "r")
        data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")

    else:

        website = entry_1.get()
        for key in data:
            if key == website:
                messagebox.showinfo(title=website,
                                    message=f"The details are:\nEmail: {data[key]['email']}\nPassword: {data[key]['password']}")

            else:
                if len(website) == 0:
                    messagebox.showerror(title="Error", message="Enter The Required Website Name")
                else:

                    messagebox.showerror(title="Error", message="No such password exists for this website")


# PASSWORD GENERATOR

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    entry_3.insert(END, string=password)


# SAVE PASSWORD

def save_data():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()

    user_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="error", message="Dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Check the data",
                                       message=f"details you've entered:\n\nwebsite: {website}\nemail: {email}\npassword: {password}\n\nis it correct?")
        if is_ok:
            try:
                file = open("data.json", "r")
                data = json.load(file)

            except FileNotFoundError:
                file = open("data.json", "w")
                json.dump(user_data, file, indent=4)
                file.close()

            else:
                data.update(user_data)
                file = open("data.json", "w")
                json.dump(data, file, indent=4)
                file.close()

        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_1.focus()


# UI SETUP

window_1 = Tk()
window_1.title("Password Manager")
window_1.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.config(padx=10, pady=10)
label_website.grid(column=0, row=1)

label_user_name = Label(text="Email/Username:")
label_user_name.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.config(padx=10, pady=10)
label_password.grid(column=0, row=3)

entry_1 = Entry(width=32)
entry_1.focus()
entry_1.grid(column=1, row=1)

entry_2 = Entry(width=51)
entry_2.grid(column=1, row=2, columnspan=2)

entry_3 = Entry(width=32)
entry_3.grid(column=1, row=3)

button_1 = Button(text="Generate Password", bg="white", command=password_generator)
button_1.grid(column=2, row=3)

button_2 = Button(text="Add", width=43, bg="white", command=save_data)
button_2.grid(column=1, columnspan=2, row=4)

search_button = Button(text="search", bg="white", width=15, command=find_password)
search_button.grid(column=2, row=1)

window_1.mainloop()
