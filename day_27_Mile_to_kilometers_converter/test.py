import tkinter

# ============================
# working with *args
# def add(*args):
#     sumsum = 0
#     for n in args:
#         sumsum += n
#     print(sumsum)
#
# add(1, 1, 1, 1, 1)
# ============================


def button_clicked():
    # my_label = tkinter.Label(text="I got clicked", font=("Arial", 24))
    # my_label.pack()
    new_user_input = user_input.get()
    my_first_label.config(text=new_user_input)


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


my_first_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_first_label.grid(column=0, row=0)

user_input = tkinter.Entry(window, width=10)
user_input.grid(column=3, row=2)

button = tkinter.Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)
new_button = tkinter.Button(text="Button 2")
new_button.grid(column=2, row=0)

window.mainloop()
