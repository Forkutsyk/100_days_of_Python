from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
DATABASE = "data\\french_words.csv"


# ---------------------------- save progress ------------------------------- #

# TODO: make possible to save wordlist to words_to_learn.csv and then if the file exist to use that file as db
def i_know(data, known_word):
    data.pop(known_word)
    df = pandas.DataFrame(data)
    print(df)
    #df.to_csv('words_to_learn.csv', index=False)
    generate_word()
# ---------------------------- flip card queue ------------------------------- #


def flip_card(data_frame, french_word):
    english = data_frame.loc[data_frame.French == french_word, 'English'].values[0]

    canvas.itemconfig(word, text=english)
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(title, fill="white")
    canvas.itemconfig(word, fill="white")
    canvas.itemconfig(title, text="English")


# ---------------------------- Generate word ------------------------------- #


def generate_word():
    data = pandas.read_csv("data\\french_words.csv")
    french_dict = data.French.to_dict()
    print(french_dict)
    random_word = random.choice(french_dict)

    canvas.itemconfig(word, text=random_word)
    canvas.itemconfig(card, image=front_card_image)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(word, fill="black")
    canvas.itemconfig(title, text="French")
    window.after(3000, flip_card, data, random_word)


# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, width=1000, height=1000)

# images
front_card_image = PhotoImage(file="images\card_front.png")
back_card_image = PhotoImage(file="images\card_back.png")
right_button_image = PhotoImage(file="images\\right.png")
wrong_button_image = PhotoImage(file="images\wrong.png")

# flashcard
canvas = Canvas(window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 267, image=front_card_image)
title = canvas.create_text(400, 130, font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 267, font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
start_button = Button(window,
                      image=right_button_image,
                      bg=BACKGROUND_COLOR,
                      highlightthickness=0,
                      command=generate_word)
start_button.grid(column=0, row=1)

reset_button = Button(window,
                      image=wrong_button_image,
                      bg=BACKGROUND_COLOR,
                      highlightthickness=0,
                      command=generate_word)
reset_button.grid(column=1, row=1)

# functions
generate_word()
mainloop()
