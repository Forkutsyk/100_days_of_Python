import json
from tkinter import *
import string
from random import randint, shuffle, choice
from tkinter import messagebox
import pyperclip

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    print("Creating the password...\n")
    elements = []
    elements += [choice(string.ascii_letters) for _ in range(randint(6, 8))]
    elements += [choice(string.punctuation) for _ in range(randint(4, 6))]
    elements += [str(randint(0, 9)) for _ in range(randint(4, 6))]
    # testing
    # print(f"Generated letters...{elements}")
    # print(f"Generated symbols...{elements}")
    # print(f"Generated numbers...{elements}")

    shuffle(elements)
    final_result = ''.join(elements)
    print(f"Result: {final_result}")

    entry_password.delete(0, END)
    pyperclip.copy(final_result)
    entry_password.insert(END, final_result)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clean_entries():
    entry_website.delete(0, END)
    entry_password.delete(0, END)


def dump_to_file(new_data):
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)
        clean_entries()


def search():
    website_search = entry_website.get()
    if website_search != "":
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                if website_search in data:
                    message = f"""
                    Email: {data[website_search]["email"]}
                    Password: {data[website_search]["password"]}
                    """
                    messagebox.showinfo(website_search, message)
                    pyperclip.copy(data[website_search]["password"])
                else:
                    messagebox.showinfo("Error",f"There are no entry: {website_search}")

        except FileNotFoundError:
            messagebox.showinfo("Error", "No Data File Found")
    else:
        messagebox.showinfo("Oops", "fill the 'website' field to search")


def save_password():
    entries = [entry_website.get(), entry_email.get(), entry_password.get()]
    new_data = {
        entries[0]: {
            "email": entries[1],
            "password": entries[2]
        }
    }

    if "" not in entries:
        try:
            with open("data.json", mode="r") as data_file:
                print("Saving ...")
                data = json.load(data_file)
                data.update(new_data)
            dump_to_file(data)

        except FileNotFoundError:
            dump_to_file(new_data)

    else:
        print("Popup ...")
        messagebox.showinfo("Oops", "Please don't leave any field empty! ")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

website_label = Label(window, text="Website:", font=(FONT_NAME, 14))
website_label.grid(column=0, row=1, padx=5, pady=5, sticky="E")
entry_website = Entry(window, width=32)
entry_website.focus()
entry_website.grid(column=1, row=1, padx=5, pady=5, sticky="W")
search_button = Button(window, text="Search", width=15, command=search)
search_button.grid(column=2, row=1, padx=5, pady=5, sticky="W")


email_label = Label(window, text="Email/Username:", font=(FONT_NAME, 14))
email_label.grid(column=0, row=2, padx=5, pady=5, sticky="E")
entry_email = Entry(window, width=52)
entry_email.insert(END, "test@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky="W")

password_label = Label(window, text="Password", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3, padx=5, pady=5, sticky="E")
entry_password = Entry(window, width=32)
entry_password.grid(column=1, row=3, padx=5, pady=5, sticky="W")
generate_button = Button(window, text="Generate Password", width=15, command=password_generator)
generate_button.grid(column=2, row=3, padx=5, pady=5, sticky="W")

add_button = Button(window, text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, padx=5, pady=5, sticky="W")

window.mainloop()
