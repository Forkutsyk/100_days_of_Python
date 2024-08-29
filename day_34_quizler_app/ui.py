from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
BUTTON_PAD = 5
FONT = "Arial"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        true_button_image = PhotoImage(file="images/true.png")
        false_button_image = PhotoImage(file="images/false.png")

        self.score = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", font=(FONT, 14))
        self.score.grid(column=1, row=0, columnspan=2)

        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill="black",
            font=(FONT, 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = Button(self.window,
                                  image=true_button_image,
                                  command=self.check_if_true,
                                  highlightthickness=0)
        self.false_button = Button(self.window,
                                   image=false_button_image,
                                   highlightthickness=0,
                                   command=self.check_if_false
                                   )
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_if_true(self):
        result = self.quiz.check_answer("True")
        self.give_feedback(result)

    def check_if_false(self):
        result = self.quiz.check_answer("False")
        self.give_feedback(result)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
