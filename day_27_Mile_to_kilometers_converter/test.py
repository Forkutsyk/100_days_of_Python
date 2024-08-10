import tkinter


def add(*args):
    sumsum = 0
    for n in args:
        sumsum += n
    print(sumsum)


add(1, 1, 1, 1, 1)

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.pack()

window.mainloop()
