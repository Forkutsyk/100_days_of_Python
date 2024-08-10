from tkinter import *


def converter():
    miles = float(user_input.get())
    miles = miles * 1.609
    km_number.config(text=miles)


root = Tk()
root.minsize(width=300, height=130)
root.config(padx=20, pady=20)
root.title("Mile to Km Converter")

user_input = Entry(root, width=10)
user_input.grid(column=1, row=0)

my_first_label = Label(root, text="Miles", font=("Arial", 14))
my_first_label.grid(column=2, row=0)

is_equal_to = Label(root, text="is equal to:", font=("Arial", 14))
is_equal_to.grid(column=0, row=1)

km_number = Label(root, text="0", font=("Arial", 14))
km_number.grid(column=1, row=1)

km_symbol = Label(root, text="Km", font=("Arial", 14))
km_symbol.grid(column=2, row=1)

new_button = Button(root, text="Calculate", command=converter)
new_button.grid(column=1, row=2)

root.mainloop()
