from tkinter import *
import string
from random import randint,shuffle,choice
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


def save_password():
    entries = [entry_website.get(), entry_email.get(), entry_password.get()]

    if "" not in entries:
        # TODO: make the function to check weather there are such entry , if yes to ask does he would like to rewrite it

        with open("passwords.txt", mode="a") as db:
            message_text = f"""
            Email: {entries[1]}
            Password: {entries[2]}
            Is this ok?
            """
            result = messagebox.askyesno(title=f"{entries[0]}", message=message_text)
            if result:
                print("Saving ...")
                entry = f"{entry_website.get()} | {entry_email.get()} | {entry_password.get()}\n"
                db.write(entry)
                clean_entries()
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
entry_website = Entry(window, width=52)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2, padx=5, pady=5, sticky="W")

email_label = Label(window, text="Email/Username:", font=(FONT_NAME, 14))
email_label.grid(column=0, row=2, padx=5, pady=5, sticky="E")
entry_email = Entry(window, width=52)
entry_email.insert(END, "test@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky="W")

password_label = Label(window, text="Password", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3, padx=5, pady=5, sticky="E")
entry_password = Entry(window, width=25)
entry_password.grid(column=1, row=3, padx=5, pady=5, sticky="W")
generate_button = Button(window, text="Generate Password", width=15, command=password_generator)
generate_button.grid(column=2, row=3, padx=5, pady=5, sticky="W")

add_button = Button(window, text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, padx=5, pady=5, sticky="W")

window.mainloop()
