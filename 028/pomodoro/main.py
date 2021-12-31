from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_action():
    global reps
    global timer
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_symbol.config(text="")
    reps = 0


def start_action():
    global reps
    global timer
    if not timer:
        if (reps % 2) == 0:
            title_label.config(text="Work", fg=GREEN)
            minutes = WORK_MIN
        elif (reps % 7) == 0:
            title_label.config(text="Break", fg=RED)
            minutes = LONG_BREAK_MIN
        else:
            title_label.config(text="Break", fg=PINK)
            minutes = SHORT_BREAK_MIN
        reps += 1
        check_string = ""
        for _ in range(reps // 2):
            check_string += "✅"
        check_symbol.config(text=check_string)
        create_timer(minutes)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def create_timer(minutes=WORK_MIN):
    seconds = minutes * 60
    countdown(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count=100):
    global timer
    minutes = str((count // 60)).zfill(2)
    seconds = str((count % 60)).zfill(2)
    time_string = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time_string)
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        timer = None
        start_action()

# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()
window.title("Pomodoro")

directory = os.path.realpath(__file__ + f"/{os.pardir}")
tomato_img = PhotoImage(file=f"{directory}/tomato.png")

window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer")
title_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"), padx=10, pady=10)
title_label.grid(column=1, row=0)

check_symbol = Label(text="", fg=GREEN, bg=YELLOW)
check_symbol.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"), padx=10, pady=10)
check_symbol.grid(column=1, row=2)

start_button = Button(text="Start", command=start_action, pady=20, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_action, pady=20, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()