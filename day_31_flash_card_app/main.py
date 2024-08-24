from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
BLACK = "black"
WHITE = "white"


class FlashCardApp:
    def __init__(self):
        try:
            self.data = pandas.read_csv("data/words_to_learn.csv")
            # print("words_to_learn")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/french_words.csv")
            # print("french_words")
        except pandas.errors.EmptyDataError:
            self.data = pandas.read_csv("data/french_words.csv")
        self.data_dic = self.data.to_dict(orient="records")
        self.current_card = {}

        # ---------------------------- UI SETUP ------------------------------- #

        # window
        self.window = Tk()
        self.window.title("Flash card")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # images
        self.front_card_image = PhotoImage(file="images/card_front.png")
        self.back_card_image = PhotoImage(file="images/card_back.png")
        self.right_button_image = PhotoImage(file="images/right.png")
        self.wrong_button_image = PhotoImage(file="images/wrong.png")

        # flashcard
        self.canvas = Canvas(self.window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.card = self.canvas.create_image(400, 267, image=self.front_card_image)
        self.title = self.canvas.create_text(400, 130, font=(FONT_NAME, 40, "italic"))
        self.word = self.canvas.create_text(400, 267, font=(FONT_NAME, 60, "bold"))
        self.canvas.grid(column=0, row=0, columnspan=2)

        # buttons
        self.start_button = Button(self.window,
                                   image=self.right_button_image,
                                   bg=BACKGROUND_COLOR,
                                   highlightthickness=0,
                                   command=self.i_know)
        self.start_button.grid(column=0, row=1)

        self.reset_button = Button(self.window,
                                   image=self.wrong_button_image,
                                   bg=BACKGROUND_COLOR,
                                   highlightthickness=0,
                                   command=self.generate_word)
        self.reset_button.grid(column=1, row=1)
        self.timer = None
        self.generate_word()

    def update_ui(self, text, image, title_color, word_color, title_text):
        self.canvas.itemconfig(self.word, text=text, fill=word_color)
        self.canvas.itemconfig(self.card, image=image)
        self.canvas.itemconfig(self.title, fill=title_color, text=title_text)

    def i_know(self):
        self.data_dic.remove(self.current_card)
        df = pandas.DataFrame(self.data_dic)
        df.to_csv('data/words_to_learn.csv', index=False)
        self.generate_word()

    def generate_word(self):
        if len(self.data_dic) == 0:
            messagebox.showinfo("Well done!", f"There are none word to learn. Well done!")
            exit()

        if self.timer:
            self.window.after_cancel(self.timer)

        self.current_card = random.choice(self.data_dic)

        self.update_ui(text=self.current_card['French'],
                       word_color=BLACK,
                       image=self.front_card_image,
                       title_color=BLACK,
                       title_text="French")

        # print(len(self.data_dic))
        self.timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        self.update_ui(text=self.current_card['English'],
                       word_color=WHITE,
                       image=self.back_card_image,
                       title_text="English",
                       title_color=WHITE)


if __name__ == '__main__':
    app = FlashCardApp()

    mainloop()
