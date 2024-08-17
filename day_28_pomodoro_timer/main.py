from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps

    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    print(reps)
    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps in range(1, 8, 2):
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps in range(2, 8, 2):
            checkmark_char = "✔" * (reps//2)
            checkmark.config(text=checkmark_char)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

title = Label(window, text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(window, text="Start", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
checkmark.grid(column=1, row=3)

window.mainloop()
