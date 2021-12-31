import os
from tkinter import *
import pandas
from random import randint

from pandas.core.frame import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
CARD_TITLE_FONT = ("Ariel", 40, "italic")
CARD_WORD_FONT = ("Ariel", 60, "bold")
TARGET_LANGUAGE="korean"
USER_LANGUAGE="english"

directory = os.path.realpath(__file__ + f"/{os.pardir}")

try:
    word_data = pandas.read_csv(f"{directory}/data/{TARGET_LANGUAGE}_words_to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv(f"{directory}/data/{TARGET_LANGUAGE}_words.csv")

words = word_data.to_dict(orient="records")

def random_word():
    random_word_index = randint(0, len(words) - 1)
    word = words[random_word_index]
    return word

def correct_button_action():
    global wait_before_flip
    global wait_before_new_word
    global words
    global current_word

    try:
        words.remove(current_word)
        new_data = DataFrame.from_dict(words)
        new_data.to_csv(f"{directory}/data/{TARGET_LANGUAGE}_words_to_learn.csv", index=False)
    except ValueError:
        pass

    if is_card_front:
        window.after_cancel(wait_before_flip)
        flip_card()
        wait_before_new_word = window.after(3000, new_word)
    else:
        try:
            window.after_cancel(wait_before_new_word)
        except NameError:
            pass
        new_word()

def wrong_button_action():
    global wait_before_flip
    global wait_before_new_word
    if is_card_front:
        window.after_cancel(wait_before_flip)
        flip_card()
        wait_before_new_word = window.after(3000, new_word)
    else:
        try:
            window.after_cancel(wait_before_new_word)
        except NameError:
            pass
        new_word()

def new_word():
    global current_word
    global wait_before_flip
    if is_card_front == False:
        current_word = random_word()
        target_language_word = current_word[TARGET_LANGUAGE.title()]
        card.itemconfig(word_text, text=target_language_word)
        flip_card()
        wait_before_flip = window.after(3000, flip_card)

def flip_card():
    global is_card_front
    global wait_before_flip
    if is_card_front:
        card.itemconfig(card_gui, image=card_back_img)
        card.itemconfig(word_text, text=current_word[USER_LANGUAGE.title()], fill="white")
        card.itemconfig(title_text, text=USER_LANGUAGE.title(), fill="white")
        is_card_front = False
    else:
        card.itemconfig(card_gui, image=card_front_img)
        card.itemconfig(word_text, text=current_word[TARGET_LANGUAGE.title()], fill="black")
        card.itemconfig(title_text, text=TARGET_LANGUAGE.title(), fill="black")
        is_card_front = True

current_word = random_word()
is_card_front = True

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file=f"{directory}/images/card_back.png")
card_front_img = PhotoImage(file=f"{directory}/images/card_front.png")
right_img = PhotoImage(file=f"{directory}/images/right.png")
wrong_img = PhotoImage(file=f"{directory}/images/wrong.png")

card = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_gui = card.create_image(400, 263, image=card_front_img)
card.grid(column=0, row=0, columnspan=2)

title_text = card.create_text(400, 150, text=f"{TARGET_LANGUAGE.title()}", fill="black", font=CARD_TITLE_FONT)
word_text = card.create_text(400, 263, text=current_word[TARGET_LANGUAGE.title()], fill="black", font=CARD_WORD_FONT)

correct_button = Button(text="correct", command=correct_button_action, image=right_img, highlightthickness=0, borderwidth=0)
correct_button.grid(column=0, row=1)

wrong_button = Button(text="wrong", command=wrong_button_action, image=wrong_img, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=1, row=1)

wait_before_flip = window.after(3000, flip_card)

window.mainloop()
